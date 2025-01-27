## 🚀 **Outil VPN CLI - TRHACKNON**

<p align="center">
  <img src="https://h.top4top.io/p_33147h2fw0.jpg" alt="Logo" width="300"/>
</p>
Bienvenue dans l'outil VPN CLI par **TRHACKNON** !  
Un outil ultra puissant et fun pour gérer tes connexions VPN avec des options flexibles pour WireGuard et OpenVPN. Tout ça, directement depuis ton terminal !

## 🛠️ **Fonctionnalités**

Voici ce que tu peux faire avec cet outil magique : 

- **Installer un VPN** : Tu peux installer facilement **WireGuard** ou **OpenVPN** sur ta machine.
- **Générer des clés WireGuard** : Crée des clés privées et publiques pour ton serveur WireGuard.
- **Créer une configuration client WireGuard** : Génère automatiquement une configuration client pour te connecter à ton serveur WireGuard via un fichier `.conf`.
- **Gérer des serveurs** : Ajoute de manière interactive des serveurs VPN dans un fichier JSON pour les gérer facilement.
- **Mode interactif** : Si tu veux un peu plus de fun, lance l'outil en mode interactif et choisis tes actions avec des menus.

## 🎨 **Installation**

Avant tout, assure-toi d'avoir **Python** et **pip** installés sur ta machine. Ensuite, installe les dépendances :

```bash
pip install -r requirements.txt
```

Une fois les dépendances installées, tu es prêt à utiliser l'outil !

🏃‍♂️ Utilisation rapide

Lance l'outil via la ligne de commande avec l'une de ces options :

🔹 Mode interactif

Lance l'outil en mode interactif pour une expérience plus agréable :

```bash
python vpn_tool.py --interactive
```

🔹 Installer un VPN

Tu peux installer WireGuard ou OpenVPN :

```bash
python vpn_tool.py --install wireguard
```

```bash
python vpn_tool.py --install openvpn
```

🔹 Générer des clés WireGuard

Si tu veux générer des clés WireGuard, spécifie un répertoire de sortie :

```bash
python vpn_tool.py --gen-keys /path/to/output/dir
```

🔹 Créer une configuration client WireGuard

Si tu veux générer une configuration pour un client WireGuard, tu dois entrer l'adresse IP du serveur, le port, ta clé privée, et la clé publique du serveur. Le fichier de configuration sera généré à l'endroit que tu indiques :

```bash
python vpn_tool.py --wg-client-config <SERVER_IP> <PORT> <PRIVATE_KEY> <PUBLIC_KEY> <OUTPUT_FILE>
```

🔹 Ajouter un serveur (multi-serveurs)

Ajoute un serveur VPN dans un fichier JSON avec cette commande :

```bash
python vpn_tool.py --add-server "server_name" "server_ip" "tcp/udp" "port"
```

⚙️ Détails techniques

Génération des clés WireGuard

Cet outil utilise la commande wg pour générer les clés privées et publiques de WireGuard. Le processus crée un fichier privatekey et un fichier publickey que tu peux utiliser dans la configuration de ton serveur.

Création de la configuration client WireGuard

La fonction create_wireguard_client_config génère un fichier de configuration .conf pour un client WireGuard, avec les clés privées et publiques, l'adresse IP du serveur, et les paramètres nécessaires pour établir une connexion VPN.

Gestion des serveurs

L'outil permet de gérer plusieurs serveurs VPN dans un fichier JSON. Tu peux ajouter un serveur avec des informations telles que le nom, l'adresse IP, le protocole et le port. Ces informations sont stockées de manière structurée pour être facilement accessibles et gérables.

🎉 Fun et personnalisation

L'outil a été conçu pour être flexible et amusant à utiliser, avec un menu interactif et des options intuitives. Tu peux choisir les différentes actions via des menus, rendant l'expérience plus agréable et interactive !

📄 License

Cet outil est distribué sous la licence MIT. Si tu as des suggestions ou des améliorations à proposer, n'hésite pas à ouvrir une issue ou à soumettre une pull request !


---

Merci d'avoir utilisé l'outil VPN CLI de TRHACKNON !
Amuse-toi bien et sois sécurisé en ligne ! 🚀
