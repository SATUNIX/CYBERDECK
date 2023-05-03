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
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo privileges"
  exit
fi
url="https://dfimg.dfrobot.com/nobody/wiki/2c091433d6aa8b440d9e6fb104ae3e8f.zip"

# Set the target directory (Downloads folder)
downloads_folder="${HOME}/Downloads"

# Download the file to the Downloads folder
file_name=$(basename "${url}")
output_path="${downloads_folder}/${file_name}"
curl -L -o "${output_path}" "${url}"

# Unzip the downloaded file in the Downloads folder
unzip "${output_path}" -d "${downloads_folder}"
cd "${downloads_folder}/LCD-show-master"

# Create a systemd service file post-reboot.service
cat << EOF | sudo tee /etc/systemd/system/post-reboot.service
[Unit]
Description=Post Reboot Script
After=default.target

[Service]
Type=oneshot
ExecStart=/path/to/post_reboot_script.sh
RemainAfterExit=yes

[Install]
WantedBy=default.target
EOF

# Replace /path/to/post_reboot_script.sh with the actual path to the post_reboot_script.sh file

# Enable the service
sudo systemctl enable post-reboot.service

# Run the LCD35-show script (which reboots the system)
./LCD35-show
'
This script downloads a file from a specific URL, saves it in the Downloads folder, 
unzips it, and runs a script that configures an LCD screen. After that script is run, 
the script modifies a configuration file (/boot/config.txt) to replace a line containing the word "waveshare" with a new line, 
reboots the computer, and then stops itself from running again.
'