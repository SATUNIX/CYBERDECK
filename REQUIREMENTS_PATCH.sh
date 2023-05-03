#!/bin/bash 


# Install required packages
sudo apt update
sudo apt install -y python3-pip bettercap tshark hashcat nmap tcpdump neofetch

# Update and install required Python modules
pip3 install --upgrade pip
pip3 install -r requirements.txt
