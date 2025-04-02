
import subprocess

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
