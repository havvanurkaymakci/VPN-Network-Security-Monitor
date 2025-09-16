VPN Network Security Monitor

📋 Proje Hakkında
Bu proje, ağ güvenliği kapsamında VPN bağlantı yönetimi ve ağ trafiği izleme işlevlerini bir arada sunan kapsamlı bir güvenlik aracıdır. Proje, kullanıcı dostu bir grafik arayüz ile VPN bağlantılarını kontrol etme, ağ paketlerini izleme ve detaylı raporlar oluşturma yeteneklerini sağlar.

🚀 Özellikler

-VPN Yönetimi
Otomatik VPN Bağlantısı: IPsec tabanlı güvenli VPN bağlantıları
Bağlantı Durumu İzleme: Real-time VPN durumu takibi
Kullanıcı Dostu Arayüz: Tkinter tabanlı grafik kullanıcı arayüzü

-Ağ İzleme ve Güvenlik
Paket Yakalama: Scapy kütüphanesi ile gerçek zamanlı paket analizi
Trafik Analizi: IP adresleri, protokoller ve paket boyutları analizi
CSV Veri Saklama: Yakalanan verilerin sistematik kaydı

-Raporlama ve Görselleştirme
Grafik Raporlar: Matplotlib ile protocol dağılımı görselleştirme
Zaman Serisi Analizi: Paket boyutlarının zamana göre değişimi
Otomatik Rapor Üretimi: PNG formatında detaylı grafikler

🛠️ Teknoloji Stack

Python 3.x: Ana programlama dili
Tkinter: Grafik kullanıcı arayüzü
Scapy: Ağ paket analizi ve yakalama
Matplotlib: Veri görselleştirme
Pandas: Veri manipülasyonu ve analizi
IPsec: VPN protokolü implementasyonu

📁 Proje Yapısı
VPN-Network-Security-Monitor/
├── main.py                    # Ana uygulama dosyası
├── vpn/
│   └── vpn_manager.py        # VPN bağlantı yönetimi
├── network_monitor/
│   └── monitor.py            # Ağ izleme modülü
├── report_generator/
│   ├── report_generator.py   # Rapor oluşturma
│   └── results/
│       └── test_results.csv  # Örnek veri dosyası
└── README.md

🔧 Kurulum ve Çalıştırma
Gereksinimler
pip install scapy matplotlib pandas tkinter

Çalıştırma
python main.py
Not: VPN işlevlerinin tam çalışması için sudo yetkilerine ihtiyaç vardır.

🎯 Kullanım Senaryoları

Ağ Güvenlik Denetimi: Kurumsal ağlarda trafik analizi
VPN Performans İzleme: Bağlantı kalitesi ve güvenlik kontrolü
Eğitim Amaçlı: Ağ güvenliği konularında pratik uygulama
Araştırma ve Geliştirme: Ağ protokollerinin analizi
