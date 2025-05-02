from scapy.all import sniff, wrpcap
import pandas as pd

# Veri saklama
timestamps = []
packet_sizes = []
packet_types = []

def packet_callback(pkt):
    timestamps.append(pkt.time)  # Zaman damgası
    packet_sizes.append(len(pkt))  # Paket boyutu
    packet_types.append(pkt.summary())  # Paket tipi (TCP/UDP/ICMP vb.)

def start_network_monitoring():
    print("Sniffing packets...")
    sniff(timeout=10, prn=packet_callback)  # 10 saniye boyunca paketleri yakala
    df = pd.DataFrame({
        'Timestamp': timestamps,
        'Packet Size': packet_sizes,
        'Packet Type': packet_types
    })
    df.to_csv("report_generator/results/test_results.csv", index=False)  # Verileri CSV'ye kaydet
    print("Packets captured to test_results.csv")

def stop_network_monitoring():
    print("Manual stop not needed with Scapy + timeout")
