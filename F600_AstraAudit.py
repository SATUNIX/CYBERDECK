"""
READ THE FOLLOWING DESCRIPTION BEFORE USING THIS PROGRAM.   
This program is a prototype and is not intended to be used in production environments.

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
"""

"""
DESCRIPTION: This script is a tool to automate the process of auditing a network.
VERSION: 3.1.1
DATE: 3/05/2021

"""
"""
This program does not have sanitised input, uses global variables, and is not thread-safe.
It is not intended to be used in production environments.
PROTOTYPE ONLY.
Further versions of this program will be developed.
"""

import os
import multiprocessing
import subprocess

"""
Requirements : tshark installed, hashcat installed, bettercap installed
Bettercap    : https://github.com/bettercap/bettercap
tshark       : https://www.wireshark.org/
hashcat      : https://hashcat.net/hashcat/
python3.10   : https://www.python.org/downloads/release/python-3100/

"""

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Bettercap:
    def __init__(self):
        self.interface = input('Enter network interface to use: ')
        self.targets = input('Enter targets to scan: ')
        self.sniffer = input('Start a sniffer? (yes/no): ').lower() == 'yes'
        self.proxy = input('Start a proxy? (yes/no): ').lower() == 'yes'
        self.redirect = input('Enter a different address to redirect all HTTP requests (leave empty for none): ')
        self.web_ui = input('Start Bettercap web UI? (yes/no): ').lower() == 'yes'
        if self.web_ui:
            self.web_ui_iface = input('Enter the network interface for the web UI: ')

    def start_bettercap(self, cmd):
        print(f'Running command: {cmd}')
        subprocess.run(cmd, shell=True)

    def execute(self):
        if self.interface:
            print(f'Using interface {self.interface}')

        if self.targets:
            print(f'Scanning targets: {self.targets}')

        if self.sniffer:
            print('Starting sniffer...')

        if self.proxy:
            print('Starting proxy...')

        if self.redirect:
            print(f'Redirecting HTTP requests to {self.redirect}')

        # Start Bettercap with the main interface
        bettercap_cmd = f'sudo bettercap -iface {self.interface}'
        bettercap_process = multiprocessing.Process(target=self.start_bettercap, args=(bettercap_cmd,))
        bettercap_process.start()

        # Start Bettercap web UI on a separate interface, if specified
        if self.web_ui:
            web_ui_cmd = f'sudo bettercap -iface {self.web_ui_iface} -caplet http-ui'
            web_ui_process = multiprocessing.Process(target=self.start_bettercap, args=(web_ui_cmd,))
            web_ui_process.start()

        bettercap_process.join()
        if self.web_ui:
            web_ui_process.join()
class Hashcat:
    def __init__(self):
        self.hashfile = input('Enter path to the hash file: ')
        self.wordlist = input('Enter path to the wordlist file: ')
        self.hash_type = input('Enter hash type (default: 0): ') or '0'
        self.attack_mode = input('Enter attack mode (default: 0): ') or '0'
        self.rules_file = input('Enter path to the rules file (leave empty for none): ')
        self.output_file = input('Enter path to the output file (leave empty for none): ')

    def execute(self):
        command = ['hashcat', '-m', self.hash_type, '-a', self.attack_mode, self.hashfile, self.wordlist]

        if self.rules_file:
            command.extend(['-r', self.rules_file])
        if self.output_file:
            command.extend(['-o', self.output_file])

        print(f'Running command: {" ".join(command)}')
        # subprocess.run(command)


class Tshark:
    def __init__(self):
        self.interface = input('Enter network interface to use: ')
        self.write = input('Enter output file to write (leave empty for none): ')
        self.filter = input('Enter capture filter (leave empty for none): ')
        self.display_filter = input('Enter display filter (leave empty for none): ')

    def execute(self):
        command = ['tshark']

        if self.interface:
            command.extend(['-i', self.interface])

        if self.write:
            command.extend(['-w', self.write])

        if self.filter:
            command.extend(['-f', self.filter])

        if self.display_filter:
            command.extend(['-Y', self.display_filter])

        print(f'Running command: {" ".join(command)}')
        # subprocess.run(command)

class Tcpdump:
    def __init__(self):
        self.interface = input('Enter network interface to use: ')
        self.write = input('Enter output file to write (leave empty for none): ')
        self.capture_filter = input('Enter capture filter (leave empty for none): ')

    def execute(self):
        command = ['tcpdump']

        if self.interface:
            command.extend(['-i', self.interface])

        if self.write:
            command.extend(['-w', self.write])

        if self.capture_filter:
            command.extend(['-f', self.capture_filter])

        print(f'Running command: {" ".join(command)}')
        # subprocess.run(command)
class Nmap:
    def __init__(self):
        self.target = input('Enter target to scan: ')
        self.scan_type = input('Enter scan type (default: -sS): ') or '-sS'
        self.port_range = input('Enter port range (leave empty for default): ')
        self.output_file = input('Enter output file to save the results (leave empty for none): ')

    def execute(self):
        command = ['nmap', self.scan_type]

        if self.port_range:
            command.extend(['-p', self.port_range])

        command.append(self.target)

        if self.output_file:
            command.extend(['-oN', self.output_file])

        print(f'Running command: {" ".join(command)}')
        # subprocess.run(command)

class Main:
    def __init__(self):
        self.execute()

    def get_valid_tool(self):
        while True:
            tool = input("\033[36mEnter the tool to use ('bettercap', 'hashcat', or 'tshark', or 'exit' to quit):\033[0m ").lower()
            if tool in ['bettercap', 'hashcat', 'tshark', 'exit']:
                return tool
            else:
                print("\033[36mInvalid input. Please enter 'bettercap', 'hashcat', 'tshark', or 'exit'.\033[0m")

    def display_ip_settings(self):
        ip_output = subprocess.check_output("ip a", shell=True).decode('utf-8')
        print("\033[36mIP Settings:\033[0m\n\033[33m", ip_output, "\033[0m")

    def execute(self):
        while True:
            clear_console()
            self.display_ip_settings()
            tool = self.get_valid_tool()

            if tool == 'bettercap':
                bettercap = Bettercap()
                bettercap.execute()
            elif tool == 'hashcat':
                hashcat = Hashcat()
                hashcat.execute()
            elif tool == 'tshark':
                tshark = Tshark()
                tshark.execute()
            elif tool == 'exit':
                print("\033[36mExiting...\033[0m")
                break
            else:
                print(f"\033[36mUnknown tool '{tool}', expected 'bettercap', 'hashcat', or 'tshark'.\033[0m")

            input("\n\033[36mPress Enter to continue...\033[0m")
            
if __name__ == '__main__':
    # Execute the specified tool
    Main()