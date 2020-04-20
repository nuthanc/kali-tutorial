# Practical Ethical Hacking

## From O'Reilly
* Install Virtual box and then get Kali-linux iso file
* Used Kali-linux-2019.2-amd64.iso

### Add crontab config
```
* * * * * cd /Users/nuthanc/personal_projects/kali-tutorial && /usr/local/anaconda3/bin/python git_acp.py >error
```
* Removed and added ssh-keygen

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
        * In computer, you do this via ports, item that can be opened on a machine and they are ways to communicate for certain protocols
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
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
```
* & at the end allows threading and if this wasn't used, we had to add ; to the commands
* Call using ./ipsweep.sh 192.168.1
* Write this out to a file using ./ipsweep.sh 192.168.1 > iplist.txt
* we can improve the script by adding a condition
```bash
#!/bin/bash
if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"

else
for ip in `seq 1 254`;do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
```
* Looping in one line
```bash
# Run one at a time
for ip in $(iplist.txt); do nmap -sS -p 80 -T4 $ip ; done
# Run multiple at a time(threading)
for ip in $(iplist.txt); do nmap -sS -p 80 -T4 $ip & done
```

### Python Refresher
* #!/bin/python3 so that if executed by ./first.py, it will use python3 to execute that
#### Strings
```python
# first.py
#!/bin/python3

print("Hello world")

print("""This string run 
on multiple lines""")

print("this string is" + " awesome")

```
* For running both code and commands, gedit first.py&
#### Math
```python
# math.py
#!/bin/python3
print(50 + 50)
print(50/50)
print(50//6)
```
#### Variables & Methods
```python
# math.py
#!/bin/python3

quote = "Everything is empty"
print(quote.upper())
```
#### Functions
```python
# math.py
#!/bin/python3

def hi():
    print("Hi, there")
```
#### List and Tuples
* Lists[] are mutable and Tuples() are immutable(they cannot be changed)
#### Importing modules
```python
#!/bin/python3
import sys
from datetime import datetime as dt

print(sys.version)
print(dt.now())
```
#### Advanced Strings
```python
#!/bin/python3

name = "Nuthan"
print(name[0]) #N
print(name[-1]) #n

sentence = "This is a sentence."
print(sentence[:4]) #This
print(sentence.split()) #Default delimiter is space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split) #Join every item in the list with ' ' which is the delimiter

# Escape to quote
sen = "He said, \"Give me your money\""

too_much_space = "          hello       "
print(too_much_space.strip()) #Strip the extra spaces
print(letter.lower() in word.lower())

movie = "A Team"
print("My favorite movie is {}".format(movie)
```
#### Dictionaries
* update method to add new key:value pair
#### Sockets
* Connect 2 nodes together
* In layman, Sockets are used to connect to an open port and IP address
* Don't use socket.py
```python
#gedit s.py&

#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777 #Can give whatever

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET: IPv4, SOCK_STREAM: Port
s.connect((HOST, PORT))

```
* Save it and use ncat
    * nc -nvlp 7777
    * Listen on port 7777
    * Waiting for anybody to connect to us
* python3 s.py 
* We see that connection established and closed
#### Building a Port Scanner
```python
#gedit scanner.py&

#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-"*50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
    for port in range(50,85): #Not doing 1 to 65,535
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        #print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close() 
except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit() #Allows clean exit

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

#python3 scanner.py 192.168.1.1
#Here 192.168.1.1 is my Router
#Because port 53 will be open for DNS and 80 for accessing the web interface on the Router
```

### The Five Stages of Ethical Hacking
1. Reconnaissance(Information Gathering)
    * Active
    * Passive
2. Scanning and Enumeration
    * nmap
    * nessus
    * nikto
3. Gaining access(Exploitation)
4. Maintaining access
5. Covering tracks

### Passive Recon
* Physical/Social: ![Alt text](img/passive_recon.png?raw=true "Physical/Social")
* Web/Host: ![Alt text](img/web.png?raw=true "Web/Host")

### Identifying our Target
* bugcrowd.com -> Programs
* Search for Tesla(for this course)
* Read the Program Details(especially the Targets) and remain out of Out of Scope

### Email address gathering with Hunter.io
* First item: Users, email format and breach credentials
* Tool: hunter.io
* hunter.io is for domain search, for ex. search for testla.com
* Only 20 searches a month under Free plan
* Why is it useful?
    * It gives us a list of people in the organization

### Gathering Breached Credentials with Breach-Parse
* github.com/hmaverickadams
* Tool: breach-parse
* Passwords coming from Credential dump, Darkweb
* Gathering username and passwords, password spraying

### Gathering Breached Credentials with WeLeakInfo
* weleakinfo.com
* **Seized by FBI**
* Alternatives:
    * https://www.saashub.com/we-leak-info-alternatives
    * https://snusbase.com/
    * https://www.dehashed.com/
* Look for User and Patterns
* For example, 123 on multiple, then 123! or some other pattern 

### Utilizing the Harvester
* Applications -> Information Gathering in Kali Linux
* theharvester -d tesla.com -l 500 -b google

### Information Gathering with Burp Suite
* Temporary Project -> Start Burp
* Open Firefox -> Preferences -> Network Proxy Settings -> Manual Proxy Configuration
    * HTTP proxy: 127.0.0.1 Port 8080
    * Use this proxy server for all protocols
    * OK
    * Leave Preferences Open
    * New tab: https://burp
    * Add to exception
    * Click on CA certificate -> Save file
    * Back to Preferences -> Privacy and Security -> Certificates -> View Certificates
    * Import the Downloaded certificate and check both the boxes and OK
    * Go to a website like tesla.com and we stall out
    * We see that Proxy tab of Burp is lit up in orange
* In the Burp Suite,
    * Keep forwarding
    * Change change the requests from GET to POST and then forward
    * Now turn Intercept off to see what is going on
    * In Target tab, we can see all the pages loaded and see the Request and Response

### Hunting Subdomains
* apt install sublist3r
* sublist3r -d tesla.com
* sublist3r with threads with, sublist3r -d tesla.com -t 100
* Also a website called crt.sh
    * Search for %.tesla.com (% = wildcard)
* Google Search owasp amass
    * https://github.com/OWASP/Amass
* tomnomnom httprobe to check whether websites are alive or not

### Identifying Website Technologies
* Google Search builtwith
    * https://builtwith.com/
* Search for tesla.com in there
* Add Wappalyzer firefox 
* whatweb in kali

### Google Fu
* Google Search for Google Search Syntax
    * https://ahrefs.com/blog/google-advanced-search-operators/
* site:tesla.com
* Don't want www and ir
    * site:tesla.com -www
    * site:tesla.com -www -ir
* File type
    * site:tesla.com filetype:docx
    * site:tesla.com filetype:pdf
    * site:tesla.com filetype:csv
    * site:tesla.com filetype:xlsx

### Utilizing Social Media
* LinkedIn -> Tesla -> Images -> First name, last name for email
* Badge photos, Desk photos, Twitter

### Installing Kioptrix Level 1
* Google Search Kioptrix Level 1
* From VulnHub, download it
* Also can checkout later "Vulnhub oscp boxes"
For MAC, the below link alone is sufficient
    * https://medium.com/@obikag/how-to-get-kioptrix-working-on-virtualbox-an-oscp-story-c824baf83da1
* VM settings
    * NAT setting
    * 256 or 128 MB
* Open the virtual machine configuration file of Kioptrix
    * Search for bridged and change it to nat for ethernet0.networkName

### Scanning with nmap
* Start kioptrix VM
* In kali, ifconfig and copy the first 3 octets
* netdiscover -r <1st 3 octets>.0/24
    * Using ARP to discover all the machines
    * Can ignore .1,2,254
* In my kali case,
    * ifconfig returns 192.168.1.6
    * netdiscover -r 192.168.1.0/24
        * Get 192.168.1.5 the machine which looks similar to ours
* Ctrl + l to clear the screen
* TCP 3 way handshake
    * SYN: Reach out to port and say "Hey port, are you open?"
    * SYNACK: Yeah, I am open, let's make the connection
    * ACK: Connect to it
* nmap: Scan for open port and services, process by stealth scanning(-sS)
* In stealth scan, we are doing SYN SYNACK RST(Reset instead of ACK)
* nmap -T4 -p- -A 192.168.1.5
    * T4: Choice in speed: 1 to 5, 1 really slow and 5 really fast
    * -p-: Scan all ports, this can be left entirely where it scans top 1000 ports
        * Top 1000 ports are like the most common ports, for instance port 80, 443, 139, 445
        * There are 65535 ports altogether for TCP and 65535 for UDP
        * Scan specific ports, -p 443 or -p 80,443,53
    * -A for every information like version,os,etc
* nmap --help 
    * To know more about nmap
    * TCP SYN a.k.a Stealth scan
    * -sS and -sU used 99% of the time
    * -sV: Probe open ports service/version info
    * -sC: equivalent to --script=default(Script scan)
* nmap -sU -T4 -p 192.168.1.5 (Still some error, need to check)
    * Replacing -p- with -p and removing -A
    * Because UDP takes forever to scan, since it's a connectionless protocol it does not have a instant response time
* Faster to do the below
    * nmap -T4 -p- 192.168.1.5
    * Then with the open ports
    * nmap -T4 -p 22,4444,8081 -A 192.168.1.5
* While scanning, utilize the time to get juicy info on Google, Social media etc

### Enumeration HTTP/HTTPS
* Commonly found with nmap are 80,443,139(Samba),445
* Light up with port 443, 80 and 139
* Firefox -> Preferences -> Network Proxy -> Use system proxy settings
* Navigate to the scanned ip in Firefox(It doesn't work in my case as Apache is not found)
* Take notes
    * 80/443 - 192.168.1.5 - 7:49
    * Default webpage - Apache - PHP
    * Not Found on clicking link: Important info: Apache version and at hostname
    * Information disclosure - 404 page - Screenshot
* nikto tool: Web vulnerability scanner
* nikto --help
* nikto -h http://192.168.1.5
    * -h for host
    * DoS is out of scope when we are doing penetration test
    * Interested in Overflow
    * Directory busting like /manual, /icons, /icons/README
    * Save your notes
* dirbuster and gobuster
* dirbuster&
    * Against targetURL in UI
    * http://192.168.1.5:80/
    * Select Go Faster
    * List based brute force
    * Browse and go to /usr/share/wordlists/dirbuster and select Small list
    * The above is well known directories
    * We need to know what's running in the backend to make good use of it
* While it's going, can utilize Burpsuite also with the Firefox proxy setting and Right click -> Send to Repeater
* Also in Browser, view source code and check for comments and passwords

### Enumerating SMB
* SMB is a file share
* Port 139 of nmap scan: Samba smbd (workgroup: MYGROUP)
* Go to terminal for msfconsole
```sh
msfconsole
#Metasploit: It's an exploitation Framework
search smb
use \<search_no\> or the \<module\>
#Search_no is not working, so give the module
info
options
set RHOSTS 192.168.1.5
run
```
* smbclient
```sh
# -L to list out files
smbclient -L \\\\192.168.1.5\\
# When ShareName obtained is IPC$ and ADMIN$
smbclient -L \\\\192.168.1.5\\ADMIN$
#or
smbclient -L \\\\192.168.1.5\\IPC$

```

### Enumerating SSH
* While ssh, if no matching key found, use the below
```sh
ssh 192.168.1.5 -oKexAlgorithms=+diffie-hellman-group1-sha1
# Error with this also, as there is no Cipher found
# Copy the offer from the error message and add to -c
ssh 192.168.1.5 -oKexAlgorithms=+diffie-hellman-group1-sha1 -c <1st offer>


```