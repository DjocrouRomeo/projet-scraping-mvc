
from dataclasses import dataclass
import statistics


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


def rechercher_par_nom(liste, nom):
    """Retourne la liste des étudiants dont le nom correspond (sans tenir compte de la casse)."""
    return [e for e in liste if e.Nom.lower() == nom.lower()]


def filtrer_par_filiere(liste, filiere):
    return [e for e in liste if e.filiere == filiere]


def trier_par_moyenne(liste, decroissant=True):
    return sorted(liste, key=lambda e: e.moyenne, reverse=decroissant)


def trier_par_nom(liste):
    return sorted(liste, key=lambda e: (e.Nom.lower(), e.Prenoms.lower()))


def trier_par_age(liste, decroissant=False):
    return sorted(liste, key=lambda e: e.age, reverse=decroissant)


def moyenne_generale(liste):
    if len(liste) == 0:
        return 0
    return statistics.mean(e.moyenne for e in liste)


def mediane(liste):
    if len(liste) == 0:
        return 0
    return statistics.median(e.moyenne for e in liste)


def ecart_type(liste):
    if len(liste) < 2:
        return 0
    return statistics.stdev(e.moyenne for e in liste)


def meilleur_etudiant(liste):
    if len(liste) == 0:
        return None
    return max(liste, key=lambda e: e.moyenne)


def moins_bon_etudiant(liste):
    if len(liste) == 0:
        return None
    return min(liste, key=lambda e: e.moyenne)


def taux_reussite(liste, seuil=10):
    """Pourcentage d'étudiants ayant une moyenne >= seuil."""
    if len(liste) == 0:
        return 0
    admis = [e for e in liste if e.moyenne >= seuil]
    return len(admis) / len(liste) * 100


def moyenne_par_filiere(liste):
    """Retourne un dictionnaire {filière: moyenne des étudiants de cette filière}."""
    resultat = {}
    for filiere in sorted({e.filiere for e in liste}):
        resultat[filiere] = moyenne_generale(filtrer_par_filiere(liste, filiere))
    return resultat


def repartition_par_sexe(liste):
    """Retourne un dictionnaire {sexe: effectif}."""
    resultat = {}
    for e in liste:
        resultat[e.sexe] = resultat.get(e.sexe, 0) + 1
    return resultat


def afficher_statistiques(liste):
    if len(liste) == 0:
        print("Aucune statistique : liste vide")
        return
    print("----- STATISTIQUES -----")
    print("Effectif            :", len(liste))
    print("Moyenne générale    :", round(moyenne_generale(liste), 2))
    print("Médiane             :", round(mediane(liste), 2))
    print("Écart-type          :", round(ecart_type(liste), 2))
    best = meilleur_etudiant(liste)
    worst = moins_bon_etudiant(liste)
    print("Meilleur étudiant   :", best.Nom, best.Prenoms, best.moyenne)
    print("Moins bon étudiant  :", worst.Nom, worst.Prenoms, worst.moyenne)
    print("Taux de réussite    :", round(taux_reussite(liste), 1), "%")
    for filiere, moy in moyenne_par_filiere(liste).items():
        print("Moyenne", filiere, ":", round(moy, 2))
    print("Répartition par sexe:", repartition_par_sexe(liste))


import copy


def saisir_texte(message):
    while True:
        valeur = input(message).strip()
        if valeur != "":
            return valeur
        print("La valeur ne peut pas être vide.")


def saisir_entier(message, minimum=0, maximum=120):
    while True:
        try:
            valeur = int(input(message).strip())
            if minimum <= valeur <= maximum:
                return valeur
            print("Valeur attendue entre", minimum, "et", maximum)
        except ValueError:
            print("Entrez un nombre entier.")


def saisir_reel(message, minimum=0.0, maximum=20.0):
    while True:
        try:
            valeur = float(input(message).strip().replace(",", "."))
            if minimum <= valeur <= maximum:
                return valeur
            print("Valeur attendue entre", minimum, "et", maximum)
        except ValueError:
            print("Entrez un nombre (ex : 12.5).")


def saisir_sexe(message):
    while True:
        valeur = input(message).strip().upper()
        if valeur in ("M", "F"):
            return valeur
        print("Entrez M ou F.")


def saisir_filiere(message):
    filieres = ["Genie_Logiciel", "Reseaux"]
    while True:
        print("Filières :", ", ".join(str(i + 1) + "=" + f for i, f in enumerate(filieres)))
        choix = input(message).strip()
        if choix.isdigit() and 1 <= int(choix) <= len(filieres):
            return filieres[int(choix) - 1]
        if choix in filieres:
            return choix
        print("Choix invalide.")


def saisir_etudiant(liste):
    """Demande tous les champs d'un nouvel étudiant (matricule unique)."""
    while True:
        matricule = saisir_texte("Matricule : ")
        if rechercher_etudiant(liste, matricule) is None:
            break
        print("Ce matricule existe déjà, choisissez-en un autre.")
    nom = saisir_texte("Nom : ")
    prenoms = saisir_texte("Prénoms : ")
    age = saisir_entier("Âge : ", 14, 80)
    filiere = saisir_filiere("Filière : ")
    sexe = saisir_sexe("Sexe (M/F) : ")
    email = saisir_texte("Email : ")
    moyenne = saisir_reel("Moyenne (0-20) : ")
    return Etudiant(nom, prenoms, age, filiere, sexe, matricule, email, moyenne)


# ---------------------------------------------------------------------
# Actions du menu
# ---------------------------------------------------------------------
def action_ajouter(liste):
    ajouter_etudiant(liste, saisir_etudiant(liste))


def action_rechercher(liste):
    matricule = saisir_texte("Matricule à rechercher : ")
    e = rechercher_etudiant(liste, matricule)
    if e is None:
        print("Étudiant introuvable")
    else:
        print(e)


def action_modifier(liste):
    matricule = saisir_texte("Matricule de l'étudiant à modifier : ")
    if rechercher_etudiant(liste, matricule) is None:
        print("Étudiant introuvable")
        return
    champs = {
        "1": ("Nom", lambda: saisir_texte("Nouveau nom : ")),
        "2": ("Prenoms", lambda: saisir_texte("Nouveaux prénoms : ")),
        "3": ("age", lambda: saisir_entier("Nouvel âge : ", 14, 80)),
        "4": ("filiere", lambda: saisir_filiere("Nouvelle filière : ")),
        "5": ("sexe", lambda: saisir_sexe("Nouveau sexe (M/F) : ")),
        "6": ("email", lambda: saisir_texte("Nouvel email : ")),
        "7": ("moyenne", lambda: saisir_reel("Nouvelle moyenne (0-20) : ")),
    }
    for cle, (nom_champ, _) in champs.items():
        print(cle, "-", nom_champ)
    choix = input("Champ à modifier : ").strip()
    if choix not in champs:
        print("Choix invalide")
        return
    nom_champ, saisie = champs[choix]
    modifier_etudiant(liste, matricule, nom_champ, saisie())


def action_supprimer(liste):
    matricule = saisir_texte("Matricule de l'étudiant à supprimer : ")
    supprimer_etudiant(liste, matricule)


def action_trier(liste):
    print("1 - Par moyenne (décroissante)")
    print("2 - Par nom (A-Z)")
    print("3 - Par âge (croissant)")
    choix = input("Votre choix : ").strip()
    if choix == "1":
        afficher_etudiants(trier_par_moyenne(liste))
    elif choix == "2":
        afficher_etudiants(trier_par_nom(liste))
    elif choix == "3":
        afficher_etudiants(trier_par_age(liste))
    else:
        print("Choix invalide")


def lancer_tests():
    """Tests de démonstration sur une COPIE : la vraie liste n'est pas modifiée."""
    test = copy.deepcopy(promotion)
    print("=== Recherche + modification ===")
    print(rechercher_etudiant(test, "18163627C").moyenne)
    modifier_etudiant(test, "18163627C", "moyenne", 15.0)
    print(rechercher_etudiant(test, "18163627C").moyenne)
    assert rechercher_etudiant(test, "18163627C").moyenne == 15.0

    print("\n=== Ajout (nouveau puis doublon) ===")
    nouveau = Etudiant("TEST", "Nouveau", 19, "Reseaux", "M", "18163640Z", "nouveau.test@iit.ci", 12.0)
    taille = len(test)
    assert ajouter_etudiant(test, nouveau) is True
    assert ajouter_etudiant(test, nouveau) is False
    assert len(test) == taille + 1

    print("\n=== Matricule inexistant ===")
    assert rechercher_etudiant(test, "XXXXXXX") is None
    assert modifier_etudiant(test, "XXXXXXX", "moyenne", 10) is False

    print("\n=== Suppression ===")
    assert supprimer_etudiant(test, "18163640Z") is True
    assert supprimer_etudiant(test, "18163640Z") is False
    assert len(test) == taille

    print("\n=== Tri par moyenne décroissante ===")
    afficher_etudiants(trier_par_moyenne(test))
    assert trier_par_moyenne(test)[0].moyenne == max(e.moyenne for e in test)

    print("\n=== Statistiques ===")
    afficher_statistiques(test)
    print("\nTous les tests sont passés")


def afficher_menu():
    print("\n========== GESTION DES ÉTUDIANTS IIT ==========")
    print("1 - Ajouter un étudiant")
    print("2 - Rechercher un étudiant (par matricule)")
    print("3 - Modifier un étudiant")
    print("4 - Supprimer un étudiant")
    print("5 - Afficher tous les étudiants")
    print("6 - Trier et afficher")
    print("7 - Statistiques")
    print("8 - Lancer les tests de démonstration")
    print("0 - Quitter")


def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()
        if choix == "1":
            action_ajouter(promotion)
        elif choix == "2":
            action_rechercher(promotion)
        elif choix == "3":
            action_modifier(promotion)
        elif choix == "4":
            action_supprimer(promotion)
        elif choix == "5":
            afficher_etudiants(promotion)
        elif choix == "6":
            action_trier(promotion)
        elif choix == "7":
            afficher_statistiques(promotion)
        elif choix == "8":
            lancer_tests()
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()