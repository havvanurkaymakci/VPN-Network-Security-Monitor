import os

# Function to start network monitoring with the specified tool and interface
def start_network_monitoring(interface, tool):
    print("Starting network monitoring...")
    
    if tool == "Wireshark":
        os.system(f"wireshark -i {interface}")
    elif tool == "tcpdump":
        os.system(f"tcpdump -i {interface} -w capture.pcap")
    elif tool == "Netdata":
        os.system("systemctl start netdata")
    
    print("Monitoring started.")

# Function to stop network monitoring
def stop_network_monitoring(tool):
    print("Stopping network monitoring...")
    
    if tool == "Wireshark":
        os.system("pkill wireshark")
    elif tool == "tcpdump":
        os.system("pkill tcpdump")
    elif tool == "Netdata":
        os.system("systemctl stop netdata")
    
    print("Monitoring stopped.")
