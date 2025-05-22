import matplotlib.pyplot as plt
import pandas as pd

def generate_graph_report():
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

