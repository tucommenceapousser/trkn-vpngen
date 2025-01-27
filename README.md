## 🚀 **Outil VPN CLI - TRHACKNON**

<p align="center">
  <img src="https://h.top4top.io/p_33147h2fw0.jpg" alt="Logo" width="300"/>
</p>

## Lien vers le projet GitHub

Clique sur le bouton ci-dessous pour accéder au code source complet de ce projet sur GitHub:

[![GitHub](https://img.shields.io/badge/GitHub-TRHACKNON-green)](http://trkn-vpn.0delta.cz)

## Lien vers le projet GitHub

Accède au code source complet sur GitHub avec le bouton ci-dessous:

[![Accéder au GitHub](https://commons.wikimedia.org/wiki/File:A_Hacker_Works_at_a_COmputer_in_a_Dark_Room.png)](http://trkn-vpn.0delta.cz)

Bienvenue dans l'**outil VPN CLI** développé par **TRHACKNON** !  
Un utilitaire puissant et flexible permettant de gérer facilement des connexions VPN via **WireGuard** et **OpenVPN**. Tout cela directement depuis ton terminal, dans une interface fluide et intuitive.

---

## 🛠️ **Fonctionnalités**

Voici ce que cet outil te permet de faire :

- **Installer un VPN** : Installe **WireGuard** ou **OpenVPN** de manière simple et rapide sur ta machine.
- **Générer des clés WireGuard** : Crée des clés privées et publiques pour ton serveur WireGuard en quelques commandes.
- **Créer une configuration client WireGuard** : Génère une configuration client avec un fichier `.conf` pour te connecter à ton serveur WireGuard.
- **Gérer des serveurs VPN** : Ajoute et gère facilement tes serveurs VPN dans un fichier JSON.
- **Mode interactif** : Utilise un mode interactif pour naviguer entre les options via un menu simple et agréable.

---

## 🎨 **Installation**

Avant d'installer l'outil, assure-toi d'avoir **Python** et **pip** d'installés sur ta machine. Ensuite, installe les dépendances nécessaires avec :

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
