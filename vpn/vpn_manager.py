<<<<<<< HEAD
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

=======

import subprocess
def connect_to_vpn():
    print("Simulated VPN connection")
    return True

def disconnect_from_vpn():
    print("Simulated VPN disconnection")
    return True



"""
def connect_to_vpn():
    try:
        # VPN bağlanma komutları (docker ipsec örneği)
        subprocess.run(["docker", "run", "--rm", "-d", "--name", "vpn", "-e", "VPN_IPSEC_PSK=YourSecretPassword", "-e", "VPN_USER=user", "-e", "VPN_PASSWORD=password", "-e", "SERVER_URL=your-vpn-server.com", "hwdsl2/ipsec-vpn-server"], check=True)
        print("VPN connected successfully")
        return True
    except subprocess.CalledProcessError:
        print("Failed to connect to VPN")
        return False

def disconnect_from_vpn():
    try:
        subprocess.run(["docker", "stop", "vpn"], check=True)
        print("VPN disconnected successfully")
        return True
    except subprocess.CalledProcessError:
        print("Failed to disconnect from VPN")
        return False
"""
>>>>>>> de3352d (lastcommit)
