from scapy.all import *


#Set the target IP Address and port 
target_ip = "141.11.84.145"
target_port = 53 #Commonly used for DNS


#Craft the UDP Packet
udp_packet = IP(dst=target_ip) / UDP(dport=target_port) / DNS(rd=1, qd=DNSQR(qname="example.com"))

#Send the packet and wait for a response
response = sr1(udp_packet, timeout=2)


#Check if a response was received
if response:
	print("Received response from target")
	response.show()
else:
	print("No Response received") 