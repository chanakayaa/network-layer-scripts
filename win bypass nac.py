import subprocess
import sys
import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, name, interface):
        threading.Thread.__init__(self)
        self.name = name
        self.interface = interface
        self.die = False

    def run(self):
        while not self.die:
            print(f"Changing MAC Address for {self.interface}\n\n{time.ctime()}")
            self.change_mac_address()
            print("MAC Changed\n")
            time.sleep(50)  # MAC address will change every 50 seconds

    def stop(self):
        self.die = True
        print("Stopping the thread...")

    def change_mac_address(self):
        new_mac = self.generate_random_mac()
        try:
            subprocess.call(f"netsh interface set interface \"{self.interface}\" admin=disable", shell=True)
            subprocess.call(f"reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001 /v NetworkAddress /d {new_mac} /f", shell=True)
            subprocess.call(f"netsh interface set interface \"{self.interface}\" admin=enable", shell=True)
        except Exception as e:
            print(f"Failed to change MAC address: {e}")

    def generate_random_mac(self):
        mac = [0x00, 0x1A, 0x2B, random.randint(0x00, 0x7F), random.randint(0x00, 0xFF), random.randint(0x00, 0xFF)]
        return ':'.join(map(lambda x: f"{x:02X}", mac))

if __name__ == '__main__':
    interface = "Ethernet"  # Change this to your network interface name
    f = MyThread('first', interface)
    f.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        f.stop()
        f.join()  # Wait for the thread to terminate
        print("Exiting program")
        sys.exit(0)
