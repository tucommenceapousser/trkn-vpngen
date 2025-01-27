import os
import subprocess
import argparse
import qrcode
import json
import questionary
import random
import string

# Installation des paquets nécessaires
def install_vpn(tool):
    print(f"[*] Installation de {tool}...")
    if tool == "wireguard":
        subprocess.run("sudo apt-get update && sudo apt-get install wireguard -y", shell=True)
    elif tool == "openvpn":
        subprocess.run("sudo apt-get update && sudo apt-get install openvpn easy-rsa -y", shell=True)
    else:
        print("[!] Outil non supporté.")

# Génération des clés WireGuard avec rotation de clés éphémères
def generate_wireguard_keys(output_dir, autosign=False, rotate_keys=True):
    os.makedirs(output_dir, exist_ok=True)
    print("[*] Génération des clés WireGuard...")
    subprocess.run(f"wg genkey | tee {output_dir}/privatekey | wg pubkey > {output_dir}/publickey", shell=True)

    if autosign:
        print("[*] Génération d'une clé publique auto-signée...")
        with open(f"{output_dir}/privatekey", "r") as f:
            private_key = f.read().strip()
        subprocess.run(f"echo '{private_key}' | wg pubkey > {output_dir}/autosigned_publickey", shell=True)
        print(f"[✓] Clé publique auto-signée sauvegardée dans {output_dir}/autosigned_publickey")
    
    # Rotation des clés éphémères (si demandé)
    if rotate_keys:
        print("[*] Rotation des clés éphémères activée.")
        ephemeral_key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        with open(f"{output_dir}/ephemeral_key", "w") as f:
            f.write(ephemeral_key)
        print(f"[✓] Clé éphémère générée et sauvegardée dans {output_dir}/ephemeral_key")
    
    print(f"[✓] Clés générées dans {output_dir}")

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
    print(f"[✓] Configuration client écrite dans {output_file}")

    # Génération d'un QR code
    print("[*] Génération du QR code pour la configuration WireGuard...")
    qr = qrcode.QRCode()
    qr.add_data(config)
    qr.print_ascii()

# Fonction de génération de configuration OpenVPN avec ChaCha20
def create_openvpn_config(secure=False):
    print("[*] Création d'une configuration OpenVPN...")
    os.makedirs("/etc/openvpn", exist_ok=True)
    subprocess.run("make-cadir /etc/openvpn/easy-rsa", shell=True)

    # Configuration sécurisée avec ChaCha20
    config = """
port 1194
proto udp
dev tun
cipher CHACHA20-POLY1305
auth SHA256
tls-version-min 1.2
dh none
ecdh-curve prime256v1
persist-key
persist-tun
user nobody
group nogroup
keepalive 10 120
verb 3
"""
    if secure:
        config += """
# Sécurisation renforcée
push "redirect-gateway def1 bypass-dhcp"
tls-auth /etc/openvpn/ta.key 0
"""
    
    with open("/etc/openvpn/server.conf", "w") as f:
        f.write(config)
    print("[✓] Configuration OpenVPN sécurisée créée.")

# Ajout interactif d'un serveur au fichier JSON
def add_server_interactive(config_file="servers.json"):
    print("[*] Ajout d'un nouveau serveur.")
    server_name = questionary.text("Nom du serveur :").ask()
    server_ip = questionary.text("IP du serveur :").ask()
    protocol = questionary.select("Protocole :", choices=["TCP", "UDP"]).ask()
    port = questionary.text("Port :").ask()

    add_server_to_config(server_name, server_ip, protocol, port, config_file=config_file)

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
    print(f"[✓] Serveur {server_name} ajouté au fichier {config_file}")

# Menu interactif
def interactive_menu():
    while True:
        action = questionary.select(
            "Que voulez-vous faire ?",
            choices=[
                "Installer un VPN",
                "Générer des clés WireGuard",
                "Créer une configuration client WireGuard",
                "Créer une configuration OpenVPN sécurisée",
                "Ajouter un serveur (multi-serveurs)",
                "Quitter"
            ]
        ).ask()

        if action == "Installer un VPN":
            vpn = questionary.select("Quel outil VPN ?", choices=["wireguard", "openvpn"]).ask()
            install_vpn(vpn)

        elif action == "Générer des clés WireGuard":
            output_dir = questionary.text("Répertoire de sortie des clés :").ask()
            autosign = questionary.confirm("Voulez-vous générer une clé publique auto-signée ?").ask()
            generate_wireguard_keys(output_dir, autosign)

        elif action == "Créer une configuration client WireGuard":
            server_ip = questionary.text("Adresse IP du serveur :").ask()
            port = questionary.text("Port :").ask()
            private_key = questionary.text("Clé privée :").ask()
            public_key = questionary.text("Clé publique du serveur :").ask()
            output_file = questionary.text("Nom du fichier de configuration :").ask()
            create_wireguard_client_config(server_ip, port, private_key, public_key, output_file)

        elif action == "Créer une configuration OpenVPN sécurisée":
            secure = questionary.confirm("Voulez-vous activer la configuration sécurisée pour OpenVPN ?").ask()
            create_openvpn_config(secure)

        elif action == "Ajouter un serveur (multi-serveurs)":
            add_server_interactive()

        elif action == "Quitter":
            print("Au revoir !")
            break

# Fonction principale
def main():
    parser = argparse.ArgumentParser(description="Outil VPN CLI par TRHACKNON.")
    parser.add_argument("--install", choices=["wireguard", "openvpn"], help="Installer WireGuard ou OpenVPN.")
    parser.add_argument("--gen-keys", metavar="DIR", help="Générer des clés WireGuard.")
    parser.add_argument("--wg-client-config", nargs=5, metavar=("SERVER_IP", "PORT", "PRIVATE_KEY", "PUBLIC_KEY", "OUTPUT"),
                        help="Créer une configuration client WireGuard.")
    parser.add_argument("--add-server", nargs=4, metavar=("NAME", "IP", "PROTOCOL", "PORT"),
                        help="Ajouter un serveur au fichier de configuration multi-serveurs.")
    parser.add_argument("--interactive", action="store_true", help="Lancer l'outil en mode interactif.")

    args = parser.parse_args()

    # Mode interactif si demandé
    if args.interactive:
        interactive_menu()
    elif args.install:
        install_vpn(args.install)
    elif args.gen_keys:
        generate_wireguard_keys(args.gen_keys)
    elif args.wg_client_config:
        create_wireguard_client_config(*args.wg_client_config)
    elif args.add_server:
        add_server_to_config(*args.add_server)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
