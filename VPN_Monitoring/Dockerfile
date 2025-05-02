FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*


# Çalışma dizinini belirle
WORKDIR /app

# Gereksinimlerinizi yüklemek için requirements.txt dosyasını kopyalayın
COPY requirements.txt .

# Python bağımlılıklarını yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamanızı kopyalayın
COPY . .

# Komutları tanımlayın
CMD ["python", "main.py"]
