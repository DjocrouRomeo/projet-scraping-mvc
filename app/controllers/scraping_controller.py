import os
class ScrapingController:
    def __init__(self, scraper, depot, vue_console, vue_export):
        self.scraper = scraper
        self.depot = depot
        self.vue_console = vue_console
        self.vue_export = vue_export

    def lancer(self, url, pages):
        self.vue_console.message("Scraping en cours...")
        produits = self.scraper.scraper(url, pages)
        self.depot.ajouter_plusieurs(produits)

        self.vue_console.afficher(self.depot.tous())
        if self.depot.taille() > 0:
            chemin = self.vue_export.vers_csv(self.depot.tous())
            self.vue_console.message(f"\nExport terminé : {chemin}")
        else:
            self.vue_console.message("Aucun produit récupéré.")