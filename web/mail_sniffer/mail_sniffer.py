#!/usr/bin/env python3
# Author: WittsEnd2
# Contributors: 
from scapy.all import *

def packet_callback(packet):
    if pakcet[TCP].payload:
        mail_packet = str(packet[TCP].payload)

        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print("[*] Server: %s" % packet[IP].payload)
            print("[*] %s" % packet[TCP].payload)
    print(packet.show())
    
sniff(prn=packet_callback, store=0, filter="tcp port 110 or tcp port 25 or tcp port 143")
    