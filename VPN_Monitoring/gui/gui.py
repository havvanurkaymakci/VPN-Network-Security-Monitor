
import tkinter as tk
from tkinter import messagebox
from vpn.vpn_manager import connect_to_vpn, disconnect_from_vpn
from network_monitor.monitor import start_network_monitoring, stop_network_monitoring
from report_generator.report_generator import generate_graph_report

class VPNMonitoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VPN Monitoring Tool")
        self.root.geometry("500x400")  # Boyutu kare yapmak için

        self.vpn_state = "off"

        # VPN kontrol butonları
        self.connect_button = tk.Button(self.root, text="Connect VPN", command=self.connect_vpn)
        self.connect_button.pack(pady=20)

        self.disconnect_button = tk.Button(self.root, text="Disconnect VPN", command=self.disconnect_vpn)
        self.disconnect_button.pack(pady=20)

        # Ağ izleme butonları
        self.start_monitor_button = tk.Button(self.root, text="Start Network Monitoring", command=self.start_network_monitor)
        self.start_monitor_button.pack(pady=20)

        self.stop_monitor_button = tk.Button(self.root, text="Stop Network Monitoring", command=self.stop_network_monitor)
        self.stop_monitor_button.pack(pady=20)

        # Rapor butonu
        self.generate_report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.generate_report_button.pack(pady=20)

    def connect_vpn(self):
        if self.vpn_state == "off":
            if connect_to_vpn():
                self.vpn_state = "on"
                messagebox.showinfo("Info", "VPN is ON")
        else:
            messagebox.showwarning("Warning", "VPN is already ON")

    def disconnect_vpn(self):
        if self.vpn_state == "on":
            if disconnect_from_vpn():
                self.vpn_state = "off"
                messagebox.showinfo("Info", "VPN is OFF")
        else:
            messagebox.showwarning("Warning", "VPN is already OFF")

    def start_network_monitor(self):
        start_network_monitoring()

    def stop_network_monitor(self):
        stop_network_monitoring()

    def generate_report(self):
        generate_graph_report()

def main():
    root = tk.Tk()
    app = VPNMonitoringApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
