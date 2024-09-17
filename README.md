Given that all the scripts are related to bypassing Cisco ISE with 802.1x authentication and there were issues with the port going into an off state during testing, here's a revised README for your repository:

---

# Network Layer Bypass Scripts for Cisco ISE with 802.1X Authentication

This repository contains various Python scripts designed to test and bypass Cisco Identity Services Engine (ISE) with 802.1X authentication enabled. The scripts cover a range of network layer attacks and techniques, including VLAN hopping, MAC flooding, CDP flooding, ARP spoofing, and more.

## Included Scripts

1. **VLAN Hopping Attack**: Uses double tagging to attempt to hop into a different VLAN.
2. **MAC Flooding Attack**: Floods the switch with MAC addresses to overwhelm its table and potentially bypass authentication.
3. **CDP Flooding Attack**: Floods the network with Cisco Discovery Protocol (CDP) packets to exploit protocol vulnerabilities.
4. **ARP Spoofing Attack**: Performs ARP spoofing to intercept network traffic between the victim and the gateway.
5. **DNS Query Flooding**: Sends DNS queries to the target to test response handling and potential vulnerabilities.
6. **802.1X Downgrade Attack**: Attempts to exploit weaknesses in 802.1X authentication by sending EAPOL packets.
7. **MAC Address Randomization**: Changes the MAC address of the network interface periodically to test NAC responses.

## Features

- **VLAN Hopping**: Attempts to bypass VLAN segmentation by crafting double-tagged packets.
- **MAC Flooding**: Overwhelms the switch's MAC address table to disrupt normal operations.
- **CDP Flooding**: Exploits CDP protocol vulnerabilities to gain network information.
- **ARP Spoofing**: Intercepts network traffic through ARP poisoning.
- **DNS Query Flooding**: Tests the target's DNS handling capabilities.
- **802.1X Downgrade**: Tests the robustness of 802.1X authentication.
- **MAC Address Randomization**: Helps in testing Network Access Control (NAC) systems by frequently changing the MAC address.

## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)
- Administrative privileges to modify network settings and registry entries (for some scripts)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/network-bypass-scripts.git
   cd network-bypass-scripts
   ```

2. **Install dependencies:**

   Ensure Python and the Scapy library are installed. For Scapy, run:

   ```bash
   pip install scapy
   ```

## Usage

1. **Modify and Run Scripts:**

   - Open each script in a text editor.
   - Modify variables such as `interface`, `target_ip`, `victim_mac`, etc., to suit your network environment.

2. **Running Scripts:**

   - Run the scripts with administrative privileges as required.
   - For example:

     ```bash
     python vlan_hopping_attack.py -i <interface> -t <target_ip> -vm <victim_mac> -am <attacker_mac> -ov <outer_vlan> -iv <inner_vlan> -c <count>
     ```

3. **Stopping Scripts:**

   - Most scripts handle `KeyboardInterrupt` (Ctrl+C) to stop execution gracefully.

## Notes

- During testing, you may experience network disruptions or ports going into an off state. Ensure that you have proper authorization and take necessary precautions.
- The scripts are intended for educational and testing purposes. Use responsibly in controlled environments.

## Example

To perform a VLAN hopping attack on a network interface named `"Wi-Fi"`, you might use the following command:

```bash
python vlan_hopping_attack.py -i Wi-Fi -t 192.168.1.10 -vm 00:11:22:33:44:55 -am 66:77:88:99:AA:BB -ov 100 -iv 200 -c 10
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues, feature requests, or pull requests. Contributions are welcome!

