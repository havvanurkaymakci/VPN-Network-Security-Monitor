
import subprocess

def start_network_monitoring():
    print("Starting network monitoring...")
    subprocess.run(["tcpdump", "-i", "eth0", "-w", "capture.pcap"])

def stop_network_monitoring():
    print("Stopping network monitoring...")
    subprocess.run(["pkill", "tcpdump"])
