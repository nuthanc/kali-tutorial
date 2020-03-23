# Practical Ethical Hacking

## From O'Reilly
* Install Virtual box and then get Kali-linux iso file
* Used Kali-linux-2019.2-amd64.iso

### Config:
* General
    * Name: Kali Linux, Type: Linux, Version: Linux 2.6/3.x/4.x (64-bit)
* System
    * Base Memory: 2048 MB
* Display
    * Scale Factor: 200%
    * Graphics Controller: VBoxSVGA
    * Acceleration: Enable 3D Acceleration
* Storage
    * Kali Linux.vdi in Controller:SATA
* Network
    * Bridged Adapter: en0: Wi-fi(Wireless)

### Setting up Kali Linux Repository
* Follow the instructions in https://superuser.com/questions/1410570/cant-install-anything-on-kali-linux-unable-to-locate-package
    * Update the /etc/apt/sources.list
    * apt-get update
* apt-get install tor

### Setting up Proxychains
* Purpose: To hide IP address of the source traffic and evade firewalls
* To do this:
* nano /etc/proxychains.conf
    * Uncomment dynamic_chain
    * Uncomment Proxy DNS requests - no leak for DNS data
    * Add socks5  127.0.0.1 9050 to the ProxyList
* socks5 is much faster than socks4
* **Sockets** is a logical endpoint for communication
* Start the tor service with the following command
    * service tor start
* Using **proxychains**
    * proxychains firefox www.dnsleaktest.com
    * This was not working until I commented out socks4

## Practical Ethical Hacking contents

### Introduction
* KeepNote and Greenshot for NoteKeeping

### Networking Refresher
* IPv4(Decimal)(inet) and IPv6(Hexadecimal)(inet6)
* 32 bit for IPv4 and 128 bit for IPv6
* Private IP addresses
    * 10.0.0.0 to 10.255.255.255
    * 172.16.0.0 to 172.31.255.255 (172.16/12 prefix)
    * 192.168.0.0 to 192.168.255.255 (192.168/16 prefix)
* MAC address as ether in ifconfig
    * First 3 pairs in MAC address lookup(OUI)
* TCP vs UDP
    * TCP: Connection-oriented protocol(High reliablility)
        * HTTP/HTTPS, ssh ,ftp
    * UDP: Connection-less protocol
        * Streaming service, DNS, VoIP
    * TCP 3 way handshake
        * Send SYN packet
        * Receive SYN+ACK packet
        * Finally send ACK packet
        * It's like you say hi to a neighbour, your neighbor acknowledges SYN by saying hello too, and finally you acknowledge too and that's ACK
        * After this you can start your conversation
        * In computer, you do this via ports, item that can be opened on a macine and they are ways to communicate for certain protocols
            * HTTP over port 80, HTTPS over port 443
    * Demonstrate via WireShark
        * In Kali, type wireshark& and start capture
    * Common ports: ![Alt text](img/common_ports.png?raw=true "Common ports")
* OSI model
    * Please Do Not Throw Sausage Pizza Away(PDNTSPA)Mneumonics
    1. Physical: Data cablesm cat6
    2. Data Link: Switching, MAC addresses
    3. Network: IP addresses, Routing
    4. Transport: TCP/UDP
    5. Session: Session management
    6. Presentation: WMV, JPEG, MOV
    7. Application: HTTP, SMTP
* Packet Tracer 
    * Sign Up in netacad
    * https://www.netacad.com/portal/learning
    * Download link: https://www.netacad.com/portal/resources/packet-tracer
* In Packet Tracer
    * Choose a Generic Router-PT and Switch-PT
    * Add end devices such as Laptop and PC
    * Double click on Device to configure
    ##### Go to Router config
        ###### Set up Interface ######
        * en 
            en and Tab for Enable or just en
        * sh ip interface brief (or) sh ip int bri
        # Take one of the fast ethernets ports and assign an IP address
        * conf t (or) configuration terminal
            To enter configuration mode
        * int fa(Tab) 0/0 (or) interface fastEthernet 0/0
        * ip address 192.168.0.1 255.255.255.0
        * do sh ip int bri to check links are UP or DOWN
        # To bring down a port: shutdown and to bring up: no shutdown
        * no shut
        * exit
        * exit
        * wr
            write our changes

        ###### Set up DHCP ######
        * en
        * conf t
        * service dhcp
        * ip dhcp pool MAIN
        * network 192.168.1.0 255.255.255.0
        * default-router 192.168.0.1 255.255.255.0
        * no network 192.168.1.0 255.255.255.0
            Made a typo of 192.168.1.0 instead of 192.168.0.0
        * network 192.168.0.0 255.255.255.0
        # Set the DNS server
        * dns-server 192.168.0.1
        * exit
        # Exclude an address from DHCP
        * ip dhcp exluded-address 192.168.0.1
        * exit
        * wr
        * sh run 
            To look at our configurations
    * Take the cable and connect the Router, Switch and End points
    * In config of Endpoints select DHCP for both IPv4 and IPv6
    * Go to Desktop -> Command Prompt
    * Type ipconfig

### Lab setup
* Google Search Kali Linux Custom Image Downloads - Offensive Security
* Click on Image Name to download
* For Windows, additional download of 7zip is also required
* Windows Virtual Machine settings in VMware Workstation 15
    * 4GB or 2GB
    * NAT(keep it) or Bridge
    * I copied it
    * root/toor or kali/kali

### Linux Refresher
* updatedb
* locate grub
* passwd
* ls -la
    * First line is -, then it is a file
    * If it's a d, then it is a directory
    * 3 groups, owner, group, all users
* adduser nuthan
* cat /etc/passwd
* cat /etc/shadow
* su for switch user
* su john, su root
#### Common Network Commands
* ifconfig
* iwconfig
* ping 192.168.1.1(Home Router)
* arp -a
    * It's gonna broadcast who has this IP address
    * And the relevant says its MAC address
    * ARP : way of associating IP with MAC
* netstat -ano
    * Active connections running on the machine
    * We can see what's open and what's talking
* route -n
    * Prints the routing table
#### Viewing, Creating and Editing Files
* echo "hey" > hey.txt
* echo "hello there" > hey.txt
    * This overwrites
* echo "Hello again" >> hey.txt
    * This appends
* touch newfile.txt
* nano newfile.txt
* gedit newfile.txt
#### Stopping and Starting Kali services
* apache2: Webserver
* Copy your ip address and go to browser and paste
    * You see unable to connect, since you are not running a webserver
* service apache2 start
    * Go enter your ip address again and you see some contents
* If you want to edit
    * Go to /var/www/html/index.html
    * Other files in /var/www/html
* Another simple way is
    * echo "Hello there" > hello.txt
    * python -m SimpleHTTPServer 8080
    * Go to localhost:8080 and you can see hello.txt
    * It's so easy, execute the command in the directory you want to serve
* service apache2 stop
* To keep the service on even after reboot, use **systemctl**
    * systemctl enable postgresql
#### Installing and Updating Tools
* apt update && apt upgrade
* apt install python-pip
* Go to Mozilla and search Github Impacket
* Click on SecureAuthCorp and Clone
* All install in /opt folder, so cd into it
* cd impact and pip install .
* Run psexec.py to check
#### Scripting with Bash
* Commands we'll be using: grep, cut, tr
* ping 192.168.1.1
* Only one packet with ping 192.168.1.1 -c 1
* ping 192.168.1.1 -c 1 > ip.txt
##### Narrowing down results using grep and cut
* cat ip.txt | grep "64 bytes" | cut -d " " -f 4 | tr
* cut -d " " -f 4
    * where -d is the delimiter, in this case it's a space
    * -f is the field, where the 4th field is the ip address
* tr -d ":"
    * Stands for translate
    * For taking out the delimiter colon
##### Script for ipsweep
```bash
#!/bin/bash

for ip in `seq 1 254`;do
ping -c $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
```
* & at the end allows threading and if this wasn't used, we had to add ; to the commands
* Call using ./ipsweep.sh 192.168.1
