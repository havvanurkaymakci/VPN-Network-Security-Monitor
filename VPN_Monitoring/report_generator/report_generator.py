
import matplotlib.pyplot as plt
import pandas as pd

def generate_graph_report():
    # Test verilerini CSV'den alıyoruz
    df = pd.read_csv("test_results.csv")

    # Basit bir grafik oluşturuluyor
    plt.plot(df['Timestamp'], df['Metric'])
    plt.title('Network Metrics Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Metric')
    plt.savefig("report.png")
    print("Graphical report generated.")
