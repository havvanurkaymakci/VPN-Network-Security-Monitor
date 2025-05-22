from scapy.all import sniff, IP
import csv
import threading
import os

sniff_thread = None
stop_sniff = False
csv_file = "packets.csv"

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)
        with open(csv_file, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([ip_src, ip_dst, proto, length])

def start_network_monitoring(interface="eth0"):
    global sniff_thread, stop_sniff

    if sniff_thread is not None:
        print("Packet sniffing already running.")
        return

    # CSV dosyasını başlat, varsa eski dosyayı sil
    if os.path.exists(csv_file):
        os.remove(csv_file)

    # Başlık satırını yaz
    with open(csv_file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["SrcIP", "DstIP", "Protocol", "Length"])

    stop_sniff = False

    def sniff_packets():
        sniff(iface=interface, prn=packet_callback, stop_filter=lambda x: stop_sniff)

    sniff_thread = threading.Thread(target=sniff_packets, daemon=True)
    sniff_thread.start()
    print("Started packet sniffing with Scapy.")

def stop_network_monitoring():
    global stop_sniff, sniff_thread
    if sniff_thread is None:
        print("Packet sniffing is not running.")
        return

    stop_sniff = True
    sniff_thread.join()
    sniff_thread = None
    print("Stopped packet sniffing.")

