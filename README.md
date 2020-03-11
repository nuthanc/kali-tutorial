# kali-tutorial

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
    * Add sock5  127.0.0.1 9050 to the ProxyList
* sock5 is much faster than sock4
* **Sockets** is a logical endpoint for communication
* Start the tor service with the following command
    * service tor start
* Using **proxychains**
    * proxychains firefox www.dnsleaktest.com