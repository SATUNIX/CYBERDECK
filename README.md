![image](https://user-images.githubusercontent.com/111553838/235823036-59a407e6-5495-47c8-a8ce-ac0dcb7bdf75.png)


#Tritium Cyber Defence © 2023

This software comes with absolutely no warranty or liability
# CYBERDECK MK-1.0

Files and programs to build your own cyberdeck, using these scripts for ease of use on my pi400 cyberdeck build. 
Its about as budget friendly I could get while keeping as much processing power I could squeeze out of a Pi. 
Utilising Pi's keyboard computer combo and Adafruit / DFrobot screens and drivers, I created this nifty little network auditing and packet sniffing cyberdeck. 
I showed one of my friends after a couple beers and he said it looks like a yugioh card deck, see below: 


![image](https://user-images.githubusercontent.com/111553838/235816204-10f7dd93-4c44-4003-a509-ce212c273afb.png)

#INSTALLATION

Clone the CYBERDECK repository using the following command:
'''
git clone https://github.com/SATUNIX/CYBERDECK.git
'''
Navigate to the CYBERDECK directory:
'''
cd CYBERDECK
'''
Run the scripts for different steps of the installation:
(The programs will reboot throughout several times) 
(They install drivers, edit config files, create oneshot processes etc) 
'''
sudo ./REQUIREMENTS_PATCH.sh
reboot
sudo ./LCD_INSTALLER.sh
reboot
sudo ./TPLINK_PATCH.sh
'''
Once the installation is complete, reboot the system:
'''
reboot
'''
After rebooting, the CYBERDECK tools will be available in the ~/CYBERDECK directory.
####Alternatively:
run the bineriser.sh script to have the python program run as through a shell command no matter where you are in the Linux filesystem. 
Make sure you dont move the github package or it will no longer work. 

# HARDWARE Used  
1. Pi400 - RASPBERRY PI 
2. 3.5" DFROBOT TFT For raspberry pi 
3. Adafruit Cyberdeck 
4. ANKO Battery pack or something similar with 5V - 2A USBC or USBA to USBC (pi400 takes USBC)
5. TPLINK TP-Link TL-WN722N (Version 2 or 3 is fine) 
  Save yourself some money by running my patch above. (Credit to david bombal - couldnt have done it without you) 
  My amazon package got stolen so I had to make to with a tplink instead of a $106AUD ALFA Card. 
    Whoever stole my package and altered the course of history on this project... I will find you. 
    
![image](https://user-images.githubusercontent.com/111553838/235816261-7dbdffaf-4e7a-4004-a24c-8b85e254a1d3.png)


# SOFTWARE (HOME GROWN)
F600_AstraAudit.py 
  A python tool to provide a one stop shop for CLI ease of use and configurations. 
  Trust me, when your working on a 3.5" screen, you might aswell make a program to automate small tasks. 
  //Never go full skiddy. 
  ([Final version 6.0.0] Auditing software)
  (NO DEBUGGING CURRENTLY) 
  (This software comes with absolutely no warranty or liability)
  
TRITIUM_LAN1 
  Something else I started but didnt finish
LCD CONFIG: 
  Installs the drivers, runs a script for the LCD Display, then modifys the /boot/config.txt file to rotate the display and flip the touch input (not that you need to) 
  
TPLINK_CONFIG: 
  Uses Davids patch and automates his process, Modified and simplified to run specifically on kali linux ARM machines such as what ive got. 
  
#SOFTWARE (PATCHES) 
For the TPLINK "TL-WN722N" 
The David Bombal patch: Run the shell script above using the method outlined by David Bombal on his github. My script is just an automation of this method. 

For the 3.5" LCD on ADAFRUIT CYBERDECK 
Connect to the internet or other WAN and run my patch with sudo privalages, you can check the file to make sure nothing fishy is going on. 
This is specifically for the 3.5 inch waveshare model you can edit this it will have heaops of comments in the shell script. 



#SOFTWARE (EXTERNAL)
python 3.10.0 https://www.python.org/downloads/release/python-3100/
tshark https://tshark.dev/setup/install/
hashcat https://hashcat.net/hashcat/
bettercap https://www.bettercap.org/
tcpdump https://www.tcpdump.org/
systemd networking tools (using ip a, etc) 
Kali Linux ARM 64Bit https://kali.download/arm-images/kali-2023.1/kali-linux-2023.1-raspberry-pi-arm64.img.xz
