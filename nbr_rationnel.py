from decimal import Decimal

'''Djocrou romeo christ E.
   Blé Goudé charles L.
   L1 Computer Science G2
   
while True:
    try:
        x = float(input("Entrez le premier nombre réel (x) : "))
        y = float(input("Entrez le deuxième nombre réel (y) : "))
        if x == y:
            print("Les deux nombres sont identiques, il n'y a pas d'intervalle.")
        else:
            if x > y:
                x, y = y, x
            rationnel = (x + y)/2
            print(f"\nVous avez choisi l'intervalle ]{x} ; {y}[")
            print(f"Le nombre rationnel {rationnel} existe et est compris entre x et y.")
            print(f"Vérification : {x} < {rationnel} < {y}")
    except ValueError:
        print("Erreur : Veuillez saisir des nombres valides ")'''
from dataclasses import dataclass


@dataclass
class Etudiant:
    Nom: str
    Prenoms: str
    age: int
    filiere: str
    sexe: str
    Matricule: str
    email: str
    moyenne: float


promotion = [
    Etudiant("BLE", "Junior", 17, "Genie_Logiciel", "M", "18163627C", "junior.ble@iit.ci", 13.67),
    Etudiant("Djocrou", "Romeo", 24, "Genie_Logiciel", "M", "1029838474C", "romeo.djocrou@iit.ci", 5.6),
    Etudiant("KOUASSI", "Aya", 18, "Genie_Logiciel", "F", "18163628A", "aya.kouassi@iit.ci", 15.20),
    Etudiant("TRAORE", "Moussa", 19, "Reseaux", "M", "18163629B", "moussa.traore@iit.ci", 11.50),
    Etudiant("KONE", "Fatou", 18, "Reseaux", "F", "18163630C", "fatou.kone@iit.ci", 16.80),
    Etudiant("YAO", "Kevin", 20, "Genie_Logiciel", "M", "18163631D", "kevin.yao@iit.ci", 9.75),
    Etudiant("DIALLO", "Awa", 17, "Genie_Logiciel", "F", "18163632E", "awa.diallo@iit.ci", 14.10),
    Etudiant("N'GUESSAN", "Eric", 19, "Reseaux", "M", "18163633F", "eric.nguessan@iit.ci", 8.40),
    Etudiant("COULIBALY", "Mariam", 18, "Reseaux", "F", "18163634G", "mariam.coulibaly@iit.ci", 12.90),
    Etudiant("OUATTARA", "Ibrahim", 20, "Genie_Logiciel", "M", "18163635H", "ibrahim.ouattara@iit.ci", 10.30),
    Etudiant("BAMBA", "Salimata", 19, "Reseaux", "F", "18163636I", "salimata.bamba@iit.ci", 17.00),
]


def ajouter_etudiant(liste, etudiant):
    for e in liste:
        if e.Matricule == etudiant.Matricule:
            print("Matricule déjà utilisé, ajout refusé")
            return False
    liste.append(etudiant)
    print("Étudiant ajouté")
    return True


def rechercher_etudiant(liste, matricule):
    for e in liste:
        if e.Matricule == matricule:
            return e
    return None


def modifier_etudiant(liste, matricule, champ, valeur):
    e = rechercher_etudiant(liste, matricule)
    if e is None:
        print("Étudiant introuvable")
        return False
    setattr(e, champ, valeur)
    print("Étudiant modifié")
    return True


def supprimer_etudiant(liste, matricule):
    e = rechercher_etudiant(liste, matricule)
    if e is None:
        print("Étudiant introuvable")
        return False
    liste.remove(e)
    print("Étudiant supprimé")
    return True


def afficher_etudiants(liste):
    if len(liste) == 0:
        print("Aucun étudiant enregistré")
        return
    for numero, e in enumerate(liste, start=1):
        print(numero, e.Matricule, e.Nom, e.Prenoms, e.age, e.filiere, e.sexe, e.email, e.moyenne)
    print("Total :", len(liste), "étudiants")


print(rechercher_etudiant(promotion, "18163627C").moyenne)
modifier_etudiant(promotion, "18163627C", "moyenne", 15.0)
print(rechercher_etudiant(promotion, "18163627C").moyenne)
afficher_etudiants(promotion)

