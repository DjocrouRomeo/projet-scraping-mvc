from config import CATEGORIES_HIGHTECH
from app.views.console_view import ConsoleView
from app.scraper.amazon_scraper import AmazonScraper
from app.models.database import DatabaseModel


class MainController:
    def __init__(self):
        self.view = ConsoleView()
        self.scraper = AmazonScraper()
        self.db = DatabaseModel()
        self.produits_en_memoire = []

    def run(self):
        while True:
            self.view.afficher_menu_principal()
            choix = input("Choisissez une option (1-4) : ").strip()

            if choix == "1":
                self.gerer_sub_menu_scraping()
            elif choix == "2":
                self.afficher_produits_recuperes()
            elif choix == "3":
                self.enregistrer_en_bdd()
            elif choix == "4":
                self.view.afficher_message("Fermeture de l'application. Au revoir !")
                break
            else:
                self.view.afficher_message("Option invalide, veuillez réessayer.")

    def gerer_sub_menu_scraping(self):
        while True:
            self.view.afficher_sous_menu_categories(CATEGORIES_HIGHTECH)
            choix_cat = input("Sélectionnez une sous-catégorie : ").strip()

            if choix_cat == "0":
                break
            elif choix_cat in CATEGORIES_HIGHTECH:
                nom_cat, url_cat = CATEGORIES_HIGHTECH[choix_cat]
                self.view.afficher_message(f"Scraping en cours pour '{nom_cat}' (images incluses)...")

                nouveaux_produits = self.scraper.scrapper_categorie(nom_cat, url_cat)
                self.produits_en_memoire.extend(nouveaux_produits)

                self.view.afficher_message(
                    f"{len(nouveaux_produits)} produits récupérés et sauvegardés localement avec leurs images.")
                break
            else:
                self.view.afficher_message("Choix invalide.")

    def afficher_produits_recuperes(self):
        if self.produits_en_memoire:
            self.view.afficher_message("--- Produits en mémoire vive (session actuelle) ---")
            self.view.afficher_produits(self.produits_en_memoire)
        else:
            self.view.afficher_message("--- Produits enregistrés dans la Base de Données SQLite ---")
            produits_bdd = self.db.recuperer_produits()
            self.view.afficher_produits(produits_bdd)

    def enregistrer_en_bdd(self):
        if not self.produits_en_memoire:
            self.view.afficher_message(
                "Aucun nouveau produit en mémoire à enregistrer. Lancez d'abord le scraping (Option 1).")
            return

        nb_insere = self.db.sauvegarder_produits(self.produits_en_memoire)
        self.view.afficher_message(f"Succès : {nb_insere} produits enregistrés dans 'data/produits.db'.")
        self.produits_en_memoire.clear()