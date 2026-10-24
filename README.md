# Amazon Scraper (catégorie Technologie)

Projet de web scraping en Python avec Selenium, structuré en architecture MVC.
Il récupère des produits tech d'Amazon (titre, prix, note, lien) et les exporte dans un fichier CSV.

## Architecture

- `app/models/` : `Produit` (un produit) et `Depot` (stocke la liste des produits)
- `app/scraper/` : `driver.py` (Chrome via Selenium), `amazon_scraper.py` (navigation), `parsing.py` (extraction des données)
- `app/views/` : `console_view.py` (affichage console), `export_view.py` (export CSV)
- `app/controllers/` : `scraping_controller.py` (coordonne le tout)
- `config.py` : réglages (site, pages, délai, fichier d'export)
- `main.py` : point d'entrée
- `data/` : page Amazon sauvegardée
- `exports/` : fichiers CSV générés
- `tests/` : tests

## Installation

1. Installer Python et Google Chrome.
2. Créer et activer l'environnement virtuel :

```
python -m venv .venv
.venv\Scripts\activate
```

3. Installer les dépendances :

```
pip install -r requirements.txt
```

## Utilisation

```
python main.py
```

Le résultat est écrit dans `exports/produits_tech.csv` (colonnes : titre, prix, note, url).

## Remarque

Amazon refuse les requêtes du Chrome piloté par Selenium (page « Toutes nos excuses »).
Le programme lit donc une copie de la page de résultats Amazon enregistrée dans `data/page_smartphone.html`
(`SITE = "amazon_local"` dans `config.py`).
Le mode `SITE = "amazon"` permet d'essayer le site en direct.