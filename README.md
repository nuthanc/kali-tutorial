# Practical Ethical Hacking

## From OReilly
* Install Virtual box and then get Kali-linux iso file

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