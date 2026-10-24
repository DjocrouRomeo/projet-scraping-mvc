class ConsoleView:
    def message(self, texte):
        print(texte)

    def afficher(self, produits):
        print(f"\n{len(produits)} produit(s) trouvé(s)\n")
        for i, p in enumerate(produits, start=1):
            print(f"{i}. {p.titre[:70]}")
            print(f"   Prix : {p.prix or 'n/a'} | Note : {p.note or 'n/a'}")