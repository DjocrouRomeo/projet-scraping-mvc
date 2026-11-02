# 🛒 Application Console - Scraper Amazon (Architecture MVC)

Application console développée en Python selon l'architecture **MVC (Modèle-Vue-Contrôleur)** permettant de récupérer les informations de produits sur Amazon (ou de basculer sur un mode de secours local), de les afficher en console, et de les stocker durablement dans une base de données SQLite.

---

##  Structure du Projet

```text
PythonProject/
│
├── app/
│   ├── controllers/
│   │   └── main_controller.py   # Contrôleur principal (gestion des menus et du flux)
│   ├── models/
│   │   └── database.py          # Gestion de la base de données SQLite
│   ├── scraper/
│   │   └── amazon_scraper.py    # Logique de scraping web et gestion de secours local
│   └── views/
│       └── console_view.py      # Affichage des menus et des listes de produits en console
│
├── data/
│   ├── images/                  # Dossier de stockage local des images téléchargées
│   ├── page_secours_smartphones.html # Page HTML locale de secours
│   └── produits.db              # Base de données SQLite
│
├── config.py                    # Configuration globale (chemins, headers, catégories)
├── main.py                      # Point d'entrée de l'application
└── README.md                    # Documentation du projet

Guide d'Intégration et d'Utilisation : Application MVC de Scraping Amazon
1. Introduction et Objectif du Projet
Ce projet consiste à développer une application console en Python basée sur l'architecture MVC (Modèle-Vue-Contrôleur). Son objectif principal est de collecter des données e-commerce (titres, prix, notes et images de smartphones) depuis Amazon, de gérer une tolérance aux pannes via des fichiers de secours locaux en cas de blocage, d'afficher ces informations de manière claire en console, et de les stocker durablement dans une base de données relationnelle SQLite.

2. Architecture Technique (MVC)
L'application respecte une séparation stricte des responsabilités à travers les dossiers suivants :

app/controllers/ : Contient le contrôleur principal (main_controller.py) qui fait le lien entre les actions de l'utilisateur, le scraper et la base de données.

app/models/ : Contient la gestion des données (database.py), gérant la connexion SQLite, la création de la table produits et l'insertion en masse.

app/scraper/ : Contient la logique de collecte (amazon_scraper.py), incluant la requête HTTP, le parsing HTML avec BeautifulSoup et le téléchargement local des images.

app/views/ : Contient l'interface console (console_view.py) pour l'affichage des menus et des listes formatées.

config.py : Fichier centralisant les chemins absolus (BASE_DIR, DATA_DIR, IMAGES_DIR, DB_PATH), les en-têtes HTTP (HEADERS) et les catégories ciblées.