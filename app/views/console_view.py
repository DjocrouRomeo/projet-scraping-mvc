class ConsoleView:
    @staticmethod
    def afficher_menu_principal():
        print("\n==========================================")
        print("    APPLICATION CONSOLE - SCRAPER AMAZON   ")
        print("==========================================")
        print("1. Démarrer le scraping")
        print("2. Afficher les produits scrappés (en mémoire)")
        print("3. Enregistrer dans la base de données SQLite")
        print("4. Quitter")
        print("------------------------------------------")

    @staticmethod
    def afficher_sous_menu_categories(categories):
        print("\n--- SOUS-CATÉGORIES HIGH-TECH ---")
        for cle, (nom, _) in categories.items():
            print(f"{cle}. {nom}")
        print("0. Retour au menu principal")
        print("----------------------------------")

    @staticmethod
    def afficher_produits(produits):
        if not produits:
            print("\nAucun produit à afficher.")
            return

        print(f"\nLISTE DES PRODUITS ({len(produits)}) :")
        print("-" * 80)
        for i, p in enumerate(produits, 1):
            if isinstance(p, dict):  # Produits en mémoire
                print(f"{i}. [{p['categorie']}] {p['titre'][:50]}... | Prix: {p['prix']} | Image: {p['image_path_locale']}")
            else:  # Produits depuis la BDD (tuple)
                print(f"ID {p[0]} | [{p[4]}] {p[1][:50]}... | Prix: {p[2]} | Note: {p[3]} | Image: {p[5]}")
        print("-" * 80)

    @staticmethod
    def afficher_message(message):
        print(f"\n[INFO] {message}")