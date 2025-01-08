import subprocess
import os
import sys

class NetNest:
    def __init__(self):
        self.connections = self.get_network_connections()

    def get_network_connections(self):
        try:
            result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print("Failed to retrieve network connections:", e)
            sys.exit(1)

    def display_connections(self):
        print("Available Network Connections:")
        print(self.connections)

    def enhance_connectivity(self):
        try:
            # Increase TCP/IP auto-tuning level
            subprocess.run(['netsh', 'int', 'tcp', 'set', 'global', 'autotuninglevel=normal'], check=True)

            # Enable DNS Cache
            subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dnsserver', 'name="Local Area Connection"', 'source=dhcp'], check=True)

            # Enable automatic metric
            subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'interface', 'interface=1', 'metric=automatic'], check=True)

            print("Connectivity settings have been enhanced.")
        except subprocess.CalledProcessError as e:
            print("Failed to enhance connectivity settings:", e)
            sys.exit(1)

    def run(self):
        self.display_connections()
        enhance = input("Would you like to enhance your connectivity settings? (y/n): ").strip().lower()
        if enhance == 'y':
            self.enhance_connectivity()

if __name__ == "__main__":
    netnest = NetNest()
    netnest.run()