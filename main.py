import os
import subprocess
import argparse
import qrcode
import json


# Installation des paquets nécessaires
def install_vpn(tool):
    print(f"[*] Installation de {tool}...")
    if tool == "wireguard":
        subprocess.run("sudo apt-get update && sudo apt-get install wireguard -y", shell=True)
    elif tool == "openvpn":
        subprocess.run("sudo apt-get update && sudo apt-get install openvpn easy-rsa -y", shell=True)
    else:
        print("[!] Outil non supporté.")


# Génération des clés pour WireGuard
def generate_wireguard_keys(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    print("[*] Génération des clés WireGuard...")
    subprocess.run(f"wg genkey | tee {output_dir}/privatekey | wg pubkey > {output_dir}/publickey", shell=True)
    print(f"[*] Clés générées dans {output_dir}")


# Création de configuration WireGuard client avec QR Code
def create_wireguard_client_config(server_ip, port, private_key, public_key, output_file):
    config = f"""
[Interface]
PrivateKey = {private_key}
Address = 10.0.0.2/24
DNS = 1.1.1.1

[Peer]
PublicKey = {public_key}
Endpoint = {server_ip}:{port}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""
    with open(output_file, "w") as f:
        f.write(config)
    print(f"[*] Configuration client écrite dans {output_file}")

    # Génération d'un QR code
    print("[*] Génération du QR code pour la configuration WireGuard...")
    qr = qrcode.QRCode()
    qr.add_data(config)
    qr.print_ascii()


# Création de configuration OpenVPN (serveur/client)
def create_openvpn_config():
    print("[*] Génération d'une configuration OpenVPN...")
    os.makedirs("/etc/openvpn/easy-rsa", exist_ok=True)
    subprocess.run("make-cadir /etc/openvpn/easy-rsa", shell=True)
    print("[*] Utilisez les scripts Easy-RSA pour générer la configuration serveur et client.")


# Récupération des statistiques WireGuard (IP connectées, trafic)
def get_wireguard_stats(interface):
    print(f"[*] Statistiques pour l'interface {interface}...")
    result = subprocess.run(f"wg show {interface}", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("[!] Impossible de récupérer les statistiques. Assurez-vous que WireGuard est configuré.")


# Gestion multi-serveurs (fichier JSON)
def add_server_to_config(server_name, server_ip, protocol, port, config_file="servers.json"):
    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            servers = json.load(f)
    else:
        servers = {}

    servers[server_name] = {
        "ip": server_ip,
        "protocol": protocol,
        "port": port
    }

    with open(config_file, "w") as f:
        json.dump(servers, f, indent=4)
    print(f"[*] Serveur {server_name} ajouté au fichier {config_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Outil VPN CLI pour cybersécurité.")
    parser.add_argument("--install", choices=["wireguard", "openvpn"], help="Installer WireGuard ou OpenVPN.")
    parser.add_argument("--gen-keys", metavar="DIR", help="Générer des clés WireGuard.")
    parser.add_argument("--wg-client-config", nargs=5, metavar=("SERVER_IP", "PORT", "PRIVATE_KEY", "PUBLIC_KEY", "OUTPUT"),
                        help="Créer une configuration client WireGuard.")
    parser.add_argument("--openvpn-config", action="store_true", help="Générer une configuration OpenVPN.")
    parser.add_argument("--stats", metavar="INTERFACE", help="Afficher les statistiques WireGuard.")
    parser.add_argument("--add-server", nargs=4, metavar=("NAME", "IP", "PROTOCOL", "PORT"),
                        help="Ajouter un serveur au fichier de configuration multi-serveurs.")

    args = parser.parse_args()

    if args.install:
        install_vpn(args.install)
    elif args.gen_keys:
        generate_wireguard_keys(args.gen_keys)
    elif args.wg_client_config:
        create_wireguard_client_config(*args.wg_client_config)
    elif args.openvpn_config:
        create_openvpn_config()
    elif args.stats:
        get_wireguard_stats(args.stats)
    elif args.add_server:
        add_server_to_config(*args.add_server)
    else:
        parser.print_help()
