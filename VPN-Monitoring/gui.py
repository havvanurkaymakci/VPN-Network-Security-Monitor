import tkinter as tk
from tkinter import messagebox
from network_monitor import start_network_monitoring, stop_network_monitoring
from vpn_monitor import setup_vpn
from report_generator import generate_graph_report, save_test_results

def setup_vpn_config():
    config = "your_vpn_config"  # VPN config parameters (to be defined)
    setup_vpn(config)

def start_monitoring():
    interface = interface_entry.get()
    tool = tool_dropdown.get()
    if interface and tool:
        start_network_monitoring(interface, tool)
        messagebox.showinfo("Monitoring", f"Monitoring started on {interface} using {tool}.")
    else:
        messagebox.showerror("Error", "Please select an interface and tool.")

def stop_monitoring():
    tool = tool_dropdown.get()
    if tool:
        stop_network_monitoring(tool)
        messagebox.showinfo("Monitoring", f"Monitoring stopped for {tool}.")
    else:
        messagebox.showerror("Error", "Please select a tool to stop.")

def generate_report():
    generate_graph_report()

def save_results():
    format = result_format_dropdown.get()
    save_test_results(format)

# Create the main window
window = tk.Tk()
window.title("VPN Monitoring Tool")

# Set the window size to be square (e.g., 500x500 pixels)
window.geometry("500x500")

# Add buttons and inputs to the GUI
setup_vpn_button = tk.Button(window, text="Setup VPN", command=setup_vpn_config)
setup_vpn_button.pack(pady=10)

start_monitoring_button = tk.Button(window, text="Start Monitoring", command=start_monitoring)
start_monitoring_button.pack(pady=10)

stop_monitoring_button = tk.Button(window, text="Stop Monitoring", command=stop_monitoring)
stop_monitoring_button.pack(pady=10)

generate_report_button = tk.Button(window, text="Generate Report", command=generate_report)
generate_report_button.pack(pady=10)

save_results_button = tk.Button(window, text="Save Results", command=save_results)
save_results_button.pack(pady=10)

# Dropdown for network interface selection
interface_label = tk.Label(window, text="Select Network Interface:")
interface_label.pack()

interface_entry = tk.Entry(window)
interface_entry.pack(pady=10)

# Dropdown for tool selection (Wireshark, tcpdump, Netdata)
tool_label = tk.Label(window, text="Select Monitoring Tool:")
tool_label.pack()

tool_dropdown = tk.StringVar(window)
tool_dropdown.set("Wireshark")  # Default value
tool_menu = tk.OptionMenu(window, tool_dropdown, "Wireshark", "tcpdump", "Netdata")
tool_menu.pack(pady=10)

# Dropdown for saving results format (CSV or Text)
result_format_label = tk.Label(window, text="Select Result Format:")
result_format_label.pack()

result_format_dropdown = tk.StringVar(window)
result_format_dropdown.set("CSV")  # Default value
result_format_menu = tk.OptionMenu(window, result_format_dropdown, "CSV", "Text")
result_format_menu.pack(pady=10)

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
