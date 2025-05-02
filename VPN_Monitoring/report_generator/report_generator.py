import matplotlib.pyplot as plt
import pandas as pd

def generate_graph_report():
    # Test verilerini CSV'den alıyoruz
    df = pd.read_csv("report_generator/results/test_results.csv")

    # Grafik oluşturuluyor: Paket boyutlarının zamanla nasıl değiştiğini gösteren bir grafik
    plt.plot(df['Timestamp'], df['Packet Size'])
    plt.title('Packet Size Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Packet Size (bytes)')
    plt.xticks(rotation=45)  # Zaman damgalarını daha okunabilir hale getirmek için
    plt.tight_layout()  # Grafik sınırlarını sıkıştır
    plt.savefig("report.png")
    print("Graphical report generated.")
