from scapy.all import *

# Sending ARP Requests


target_mac = "8c:94:1f:03:73:85"

broadcast = "ff:ff:ff:ff:ff:ff"

arp = ARP(op=1, pdst="141.11.82.20", hwdst=target_mac)

ether = Ether(dst=broadcast)

packet = ether/arp

while True:
	sendp(packet)