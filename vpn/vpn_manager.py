import subprocess

def connect_to_vpn(connection_name="myvpn"):
    try:
        result = subprocess.run(
            ["sudo", "ipsec", "up", connection_name],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"VPN '{connection_name}' bağlantısı başarılı.\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"VPN '{connection_name}' bağlantısı başarısız.\nHata: {e.stderr}")
        return False

def disconnect_from_vpn(connection_name="myvpn"):
    try:
        result = subprocess.run(
            ["sudo", "ipsec", "down", connection_name],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"VPN '{connection_name}' bağlantısı kesildi.\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"VPN '{connection_name}' bağlantısı kesilemedi.\nHata: {e.stderr}")
        return False

