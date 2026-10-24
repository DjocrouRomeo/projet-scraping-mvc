"""
Petit programme : gestion de stock (Exercice 1) avec pseudo-code avant le code (Exercice 3)
"""
from dataclasses import dataclass

# ---------------------------------------------------------------
# TYPE Produit = ENREGISTREMENT
#     nom       : Chaîne
#     prix      : Réel
#     quantite  : Entier
#     categorie : Chaîne
# FIN ENREGISTREMENT
# ---------------------------------------------------------------
@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int
    categorie: str


stock = [
    Produit("Riz 25kg", 15000, 20, "Alimentaire"),
    Produit("Savon", 300, 80, "Hygiène"),
    Produit("Eau minérale", 500, 3, "Boissons"),
]


# ---------------------------------------------------------------
# FONCTION rechercher(liste, nom) : Produit ou NUL
# DEBUT
#     POUR chaque p DANS liste FAIRE
#         SI p.nom = nom ALORS RETOURNER p FIN SI
#     FIN POUR
#     RETOURNER NUL
# FIN
# ---------------------------------------------------------------
def rechercher(liste, nom):
    for p in liste:
        if p.nom.lower() == nom.lower():
            return p
    return None


# ---------------------------------------------------------------
# FONCTION ajouter(liste, produit) : Booléen
# DEBUT
#     SI rechercher(liste, produit.nom) <> NUL ALORS
#         AFFICHER "Produit déjà existant"
#         RETOURNER Faux
#     FIN SI
#     liste.ajouter(produit)
#     RETOURNER Vrai
# FIN
# ---------------------------------------------------------------
def ajouter(liste, produit):
    if rechercher(liste, produit.nom) is not None:
        print("Produit déjà existant")
        return False
    liste.append(produit)
    print("Produit ajouté")
    return True


# ---------------------------------------------------------------
# FONCTION entree(liste, nom, qte) : Booléen        // on reçoit de la marchandise
# DEBUT
#     p <- rechercher(liste, nom)
#     SI p = NUL ALORS AFFICHER "Produit introuvable" ; RETOURNER Faux FIN SI
#     p.quantite <- p.quantite + qte
#     RETOURNER Vrai
# FIN
# ---------------------------------------------------------------
def entree(liste, nom, qte):
    p = rechercher(liste, nom)
    if p is None:
        print("Produit introuvable")
        return False
    p.quantite = p.quantite + qte
    print("Nouveau stock :", p.quantite)
    return True


# ---------------------------------------------------------------
# FONCTION sortie(liste, nom, qte) : Booléen        // on vend de la marchandise
# DEBUT
#     p <- rechercher(liste, nom)
#     SI p = NUL ALORS AFFICHER "Produit introuvable" ; RETOURNER Faux FIN SI
#     SI qte > p.quantite ALORS AFFICHER "Stock insuffisant" ; RETOURNER Faux FIN SI
#     p.quantite <- p.quantite - qte
#     RETOURNER Vrai
# FIN
# ---------------------------------------------------------------
def sortie(liste, nom, qte):
    p = rechercher(liste, nom)
    if p is None:
        print("Produit introuvable")
        return False
    if qte > p.quantite:
        print("Stock insuffisant, il reste", p.quantite)
        return False
    p.quantite = p.quantite - qte
    print("Nouveau stock :", p.quantite)
    return True


# ---------------------------------------------------------------
# PROCEDURE afficher(liste)
# DEBUT
#     SI taille(liste) = 0 ALORS AFFICHER "Stock vide" ; FIN SI
#     POUR chaque p DANS liste FAIRE
#         AFFICHER p.nom, p.categorie, p.prix, p.quantite
#     FIN POUR
# FIN
# ---------------------------------------------------------------
def afficher(liste):
    if len(liste) == 0:
        print("Stock vide")
        return
    for numero, p in enumerate(liste, start=1):
        print(numero, p.nom, "|", p.categorie, "|", p.prix, "FCFA | quantité :", p.quantite)


# ---------------------------------------------------------------
# FONCTION valeur_totale(liste) : Réel
# DEBUT
#     total <- 0
#     POUR chaque p DANS liste FAIRE
#         total <- total + p.prix * p.quantite
#     FIN POUR
#     RETOURNER total
# FIN
# ---------------------------------------------------------------
def valeur_totale(liste):
    total = 0
    for p in liste:
        total = total + p.prix * p.quantite
    return total


# ---------------------------------------------------------------
# MENU : l'utilisateur saisit ses données
# ---------------------------------------------------------------
def main():
    while True:
        print("\n1-Ajouter  2-Entrée  3-Sortie  4-Afficher  5-Valeur du stock  0-Quitter")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            nom = input("Nom : ")
            prix = float(input("Prix : "))
            quantite = int(input("Quantité : "))
            categorie = input("Catégorie : ")
            ajouter(stock, Produit(nom, prix, quantite, categorie))
        elif choix == "2":
            entree(stock, input("Nom du produit : "), int(input("Quantité reçue : ")))
        elif choix == "3":
            sortie(stock, input("Nom du produit : "), int(input("Quantité vendue : ")))
        elif choix == "4":
            afficher(stock)
        elif choix == "5":
            print("Valeur totale du stock :", valeur_totale(stock), "FCFA")
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide")


main()