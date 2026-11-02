import os
import requests
from bs4 import BeautifulSoup
from config import HEADERS, IMAGES_DIR, BASE_DIR


class AmazonScraper:
    def __init__(self):
        self.headers = HEADERS
        os.makedirs(IMAGES_DIR, exist_ok=True)

    def scrapper_categorie(self, nom_categorie, url):
        """Télécharge et extrait les informations des articles de la catégorie choisie."""
        produits = []
        html_content = None

        # 1. Tentative de requête en ligne
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200 and "captcha" not in response.text.lower():
                html_content = response.content
            else:
                print(f"[AVERTISSEMENT] Amazon a bloqué la requête (Code {response.status_code}).")
        except Exception as e:
            print(f"[AVERTISSEMENT] Connexion impossible à Internet ({e}).")

        # 2. Solution de secours : s'exécute si la requête web a échoué ou a été bloquée
        if not html_content:
            print(f"[INFO] Utilisation de la page de secours locale pour '{nom_categorie}'...")

            # Dictionnaire associant chaque nom de sous-catégorie à son fichier HTML dédié
            fichiers_locaux = {
                "Smartphones & Téléphones": os.path.join(BASE_DIR, "data", "page_secours_smartphones.html"),
                "Ordinateurs portables": os.path.join(BASE_DIR, "data", "page_secours_ordinateurs.html"),
                "Casques & Écouteurs Audio": os.path.join(BASE_DIR, "data", "page_secours_audio.html")
            }

            # Récupère le chemin du fichier, ou utilise les smartphones par défaut
            chemin_local = fichiers_locaux.get(
                nom_categorie,
                os.path.join(BASE_DIR, "data", "page_secours_smartphones.html")
            )

            if os.path.exists(chemin_local):
                with open(chemin_local, "rb") as f:
                    html_content = f.read()
                print(f"[INFO] Chargement réussi depuis : {os.path.basename(chemin_local)}")
            else:
                print(f"[ERREUR] Fichier introuvable : {chemin_local}")
                return produits

        # 3. Parsing du contenu HTML (qu'il vienne du web ou du fichier de secours)
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            items = soup.find_all("div", {"data-component-type": "s-search-result"})

            for idx, item in enumerate(items, 1):
                # Extraction du titre
                titre_elem = item.find("h2")
                titre = titre_elem.text.strip() if titre_elem else "Titre non spécifié"

                # Extraction du prix
                prix_elem = item.find("span", {"class": "a-price-whole"})
                prix_symbol = item.find("span", {"class": "a-price-symbol"})
                prix = f"{prix_elem.text.strip()}{prix_symbol.text.strip()}" if prix_elem and prix_symbol else "N/A"

                # Extraction de la note
                note_elem = item.find("span", {"class": "a-icon-alt"})
                note = note_elem.text.strip() if note_elem else "Pas de note"

                # Extraction du lien d'image
                img_elem = item.find("img", {"class": "s-image"})
                image_url = img_elem["src"] if img_elem else None

                # Téléchargement de l'image (ou gestion locale)
                image_path_locale = self._telecharger_image(image_url, f"{nom_categorie}_{idx}")

                produits.append({
                    "titre": titre,
                    "prix": prix,
                    "note": note,
                    "categorie": nom_categorie,
                    "image_url": image_url if image_url else "N/A",
                    "image_path_locale": image_path_locale
                })

        except Exception as e:
            print(f"Erreur durant le parsing : {e}")

        return produits

    def _telecharger_image(self, url, nom_fichier_base):
        """Télécharge l'image du produit dans le dossier local data/images/."""
        if not url or url.startswith("data:image"):
            return "Aucune image"

        try:
            res = requests.get(url, headers=self.headers, stream=True, timeout=5)
            if res.status_code == 200:
                extension = url.split('.')[-1].split('?')[0]
                if extension not in ['jpg', 'jpeg', 'png', 'webp']:
                    extension = 'jpg'

                nom_nettoye = "".join(c for c in nom_fichier_base if c.isalnum() or c in ('_', '-'))
                chemin_relatif = os.path.join("data", "images", f"{nom_nettoye}.{extension}")
                chemin_absolu = os.path.join(IMAGES_DIR, f"{nom_nettoye}.{extension}")

                with open(chemin_absolu, "wb") as f:
                    for chunk in res.iter_content(1024):
                        f.write(chunk)

                return chemin_relatif
        except Exception:
            pass
        return "Échec du téléchargement"