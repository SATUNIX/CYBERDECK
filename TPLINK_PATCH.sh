#!/bin/bash
#VERSION 1.0    
'
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'

# Define a one-shot systemd service file to run after reboot
cat << EOF | sudo tee /etc/systemd/system/rtl8188eus-install.service
[Unit]
Description=Install RTL8188EUS driver
After=default.target

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'cd /home/$(whoami)/rtl8188eus && make && make install && modprobe 8188eu'

[Install]
WantedBy=default.target
EOF

# Update and install necessary packages
sudo apt update
sudo apt upgrade
sudo apt install bc build-essential libelf-dev linux-headers-$(uname -r) dkms

# Clone and configure rtl8188eus
sudo rmmod r8188eu.ko
git clone https://github.com/aircrack-ng/rtl8188eus
cd rtl8188eus

# Add blacklist entry to realtek.conf
sudo bash -c 'echo "blacklist r8188eu" > /etc/modprobe.d/realtek.conf'

# Reboot
sudo systemctl enable rtl8188eus-install.service
sudo reboot
