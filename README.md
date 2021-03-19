# mitm_scapy_nfqueue
The goal was to create a man in the middle forward proxy which would replace all outbound requests of foo with bar

## Background

This project was undertaken as part of a job application. I created a very simple site at http://flask-env.eba-bmzmpn9t.us-east-2.elasticbeanstalk.com/ with the sole purpose of accepting a variable within the input box and sending it to the /display_text endpoint. The server will then return the same variable to the user and it will appear on the screen. When that variable is foo and is coming from the 'victim' machine my program will intercept the request and change it to bar. The technologies used (specifically nfqueue) will only work on a linux machine with python 3.6 or lower.

## Files

mitm.py: The goal of this file is to perform arp spoofing on the network so that the victim machine thinks that the attacking machine is the network gateway and the gateway thinks the attacking machine is the victim machine.

main.py: Once the network traffic has been rerouted run this file to intercept the specified packets.

the_site: A folder containing the code for the simple web application currently deployed on AWS.

## Set Up

__clone the repository:__   
git clone https://github.com/Bencabe/mitm_scapy_nfqueue.git

__nfqueue does not work with python versions later than 3.6 so I recommend creating a virtual environment. If you have anaconda:__
conda create -n mitm python=3.6   
conda activate mitm

__now install dependencies:__    
apt-get install build-essential python-dev libnetfilter-queue-dev   
pip install -r requirements.txt

__alter for your network:__      
The 'victim' machine was my laptop at ip 10.0.2.10   
the 'attacking' machine was a linux virtual machine at ip 10.0.2.47   
the gateway was at 10.0.0.1   
These ip addresses will need to be changed in the 'mitm.py' file if you are reproducing this on your home network   

## The project in action

__before the attack__   
![before](https://user-images.githubusercontent.com/44676083/111806806-435ef500-88ca-11eb-891b-ac6e93c09420.gif)


__the attack__
![during](https://user-images.githubusercontent.com/44676083/111811445-f3366180-88ce-11eb-864f-55d560ab03dc.gif)


__after the attack__
![after](https://user-images.githubusercontent.com/44676083/111807746-3098f000-88cb-11eb-90d2-e22de060a85f.gif)







