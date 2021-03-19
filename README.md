# mitm_scapy_nfqueue
The goal was to create a man in the middle forward proxy which would replace all outbound requests of foo with bar

## Background

This project was undertaken as part of a job application. I created a very simple site at http://flask-env.eba-bmzmpn9t.us-east-2.elasticbeanstalk.com/ with the sole purpose of accepting a variable within the input box and sending it to the /display_text endpoint. The server will then return the same variable to the user and it will appear on the screen. When that variable is foo and is coming from the 'victim' machine my program will intercept the request and change it to bar. The technologies used (specifically nfqueue) will only work on a linux machine with python 3.6 or lower.

## Files

mitm.py: The goal of this file is to perform arp spoofing on the network so that the victim machine thinks that attacking machine is the network gateway and the gateway thinks the attacking machine is the victim machine.

main.py: Once the network traffic has been rerouted run this file to intercept the specified packets.

the_site: A folder containing the code for the simple web application currently deployed on AWS.

## Set Up

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
https://user-images.githubusercontent.com/44676083/111799961-6639db00-88c3-11eb-9ef3-8caccbc2d4e9.mov


__the attack__
![D482D7AB-5E38-4652-9C37-7ADE939218E6_1_105_c](https://user-images.githubusercontent.com/44676083/111803354-e150c080-88c6-11eb-8695-3a74195a51ed.jpeg)


__after the attack__
![10D4EFA9-7CBE-49EE-A514-9C6E71FE9653_1_105_c](https://user-images.githubusercontent.com/44676083/111801927-57ecbe80-88c5-11eb-9086-602169d5f21c.jpeg)







