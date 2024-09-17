from scapy.all import *

# Target MAC address and broadcast address
target_mac = "xx:yy:xx:yy:xx:yy"
broadcast = "ff:ff:ff:ff:ff:ff"

# Creating an ARP request
arp = ARP(op=1, pdst="xx.xx.xx.xx", hwdst=target_mac)

# Encapsulating the ARP request into an Ethernet frame
ether = Ether(dst=broadcast)

# Combining the Ethernet and ARP layers into one packet
packet = ether / arp

# Sending the packet in an infinite loop
while True:
    sendp(packet)
