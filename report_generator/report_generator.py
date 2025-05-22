import matplotlib.pyplot as plt
import pandas as pd

def generate_graph_report():
<<<<<<< HEAD
    try:
        df = pd.read_csv("packets.csv")
    except FileNotFoundError:
        print("CSV dosyası bulunamadı.")
        return

    if df.empty or len(df) <= 1:
        print("CSV dosyası boş veya sadece başlık var.")
        return

    # Protokollere göre sayım yap
    proto_counts = df['Protocol'].value_counts()

    plt.figure(figsize=(8, 6))
    proto_counts.plot(kind='bar')
    plt.title('Protocol Distribution in Captured Packets')
    plt.xlabel('Protocol Number')
    plt.ylabel('Packet Count')
    plt.tight_layout()
    plt.savefig("report.png")
    plt.close()
    print("Graphical report generated as report.png")

=======
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
>>>>>>> de3352d (lastcommit)
