class Produit:
    TVA = 0.18
    def __init__(self, nom , prix_ht , stock):
        stock = 0
        if prix_ht <= 0:
            raise ("Le prix doit être positif")
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock

jus = Produit ("Carton de jus 12x1L",6000, 50)
riz = Produit ("Sac de riz 25kg", 17500, 50)

def prix_ttc(self):
    return round(self.prix_ht * self.TVA)

def valeur_stock(self):
    return (self.prix_ht * self.stock)


def vendre(self, quantite):  # 4 espaces
    if quantite > self.stock:
        raise ValueError(
            f"Stock insuffisant : {self.stock} disponible(s), {quantite} demandé(s)"
        )
    self.stock = self.stock - quantite
    return quantite * self.prix_ht * (1 + self.TVA)

class Produit:
    TVA = 0.18

    def __init__(self, nom, prix_ht, stock):
        if prix_ht <= 0:
            raise ValueError("Le prix doit être positif")
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock

    def vendre(self, quantite):
        ...






































































































































    def __str__(self):
        return f"{self.nom} — {self.prix_ht} FCFA HT ({self.stock} en stock)"


class Panier:
    def __init__(self, nom_client):
        self.nom_client = nom_client
        self.lignes = []

    def ajouter(self, produit, quantite):
        self.lignes.append((produit, quantite))

    def total_ttc(self):
        total = 0
        for produit, quantite in self.lignes:
            total += produit.prix_ht * (1 + produit.TVA) * quantite
        return total

if __name__ == "__main__":
    jus = Produit("Carton de jus 12x1L", 6000, 50)
    riz = Produit("Sac de riz 25kg", 15000, 20)

    panier = Panier("Maquis Chez Awa")
    panier.ajouter(jus, 2)
    panier.ajouter(riz, 1)

    print(panier.nom_client)
    print(panier.total_ttc())
    assert round(panier.total_ttc(), 2) == 31860



