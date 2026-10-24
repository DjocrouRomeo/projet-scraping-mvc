"""
Petit programme : école primaire de Yopougon (Exercice 2)
avec pseudo-code avant le code (Exercice 3)

Structure imbriquée :  Ecole -> tableau de Classe -> tableau de Eleve -> tableau de Note
"""
from dataclasses import dataclass, field

# ---------------------------------------------------------------
# TYPE Note = ENREGISTREMENT
#     matiere : Chaîne
#     valeur  : Réel                      // sur 20
# FIN ENREGISTREMENT
#
# TYPE Eleve = ENREGISTREMENT
#     matricule : Chaîne
#     nom       : Chaîne
#     prenoms   : Chaîne
#     notes     : Tableau de Note
# FIN ENREGISTREMENT
#
# TYPE Classe = ENREGISTREMENT
#     nom    : Chaîne                     // CP1, CE2, CM2...
#     eleves : Tableau de Eleve
# FIN ENREGISTREMENT
#
# TYPE Ecole = ENREGISTREMENT
#     nom     : Chaîne
#     classes : Tableau de Classe
# FIN ENREGISTREMENT
# ---------------------------------------------------------------
@dataclass
class Note:
    matiere: str
    valeur: float


@dataclass
class Eleve:
    matricule: str
    nom: str
    prenoms: str
    notes: list = field(default_factory=list)


@dataclass
class Classe:
    nom: str
    eleves: list = field(default_factory=list)


@dataclass
class Ecole:
    nom: str
    classes: list = field(default_factory=list)


ecole = Ecole("École primaire de Yopougon", [
    Classe("CP1", [
        Eleve("E001", "KOUADIO", "Ahou", [Note("Français", 14), Note("Maths", 12)]),
        Eleve("E002", "TRAORE", "Ibrahim", [Note("Français", 10), Note("Maths", 13)]),
    ]),
    Classe("CM2", [
        Eleve("E003", "COULIBALY", "Fatou", [Note("Français", 15), Note("Maths", 16)]),
    ]),
])


# ---------------------------------------------------------------
# FONCTION rechercher_classe(ecole, nom) : Classe ou NUL
# DEBUT
#     POUR chaque c DANS ecole.classes FAIRE
#         SI c.nom = nom ALORS RETOURNER c FIN SI
#     FIN POUR
#     RETOURNER NUL
# FIN
# ---------------------------------------------------------------
def rechercher_classe(ecole, nom):
    for c in ecole.classes:
        if c.nom.upper() == nom.strip().upper():
            return c
    return None


# ---------------------------------------------------------------
# FONCTION ajouter_classe(ecole, nom) : Booléen
# DEBUT
#     SI rechercher_classe(ecole, nom) <> NUL ALORS
#         AFFICHER "Classe déjà existante" ; RETOURNER Faux
#     FIN SI
#     ecole.classes.ajouter( Classe(nom, tableau vide) )
#     RETOURNER Vrai
# FIN
# ---------------------------------------------------------------
def ajouter_classe(ecole, nom):
    if rechercher_classe(ecole, nom) is not None:
        print("Classe déjà existante")
        return False
    ecole.classes.append(Classe(nom.strip().upper()))
    print("Classe ajoutée")
    return True


# ---------------------------------------------------------------
# FONCTION rechercher_eleve(ecole, matricule) : (Classe, Eleve) ou (NUL, NUL)
# DEBUT
#     POUR chaque c DANS ecole.classes FAIRE         // 1er niveau : les classes
#         POUR chaque e DANS c.eleves FAIRE           // 2e niveau : les élèves
#             SI e.matricule = matricule ALORS RETOURNER (c, e) FIN SI
#         FIN POUR
#     FIN POUR
#     RETOURNER (NUL, NUL)
# FIN
# ---------------------------------------------------------------
def rechercher_eleve(ecole, matricule):
    for classe in ecole.classes:
        for eleve in classe.eleves:
            if eleve.matricule == matricule.strip():
                return classe, eleve
    return None, None


# ---------------------------------------------------------------
# FONCTION ajouter_eleve(ecole, nom_classe, eleve) : Booléen
# DEBUT
#     c <- rechercher_classe(ecole, nom_classe)
#     SI c = NUL ALORS AFFICHER "Classe introuvable" ; RETOURNER Faux FIN SI
#     SI rechercher_eleve(ecole, eleve.matricule) <> (NUL, NUL) ALORS
#         AFFICHER "Matricule déjà utilisé" ; RETOURNER Faux
#     FIN SI
#     c.eleves.ajouter(eleve)
#     RETOURNER Vrai
# FIN
# ---------------------------------------------------------------
def ajouter_eleve(ecole, nom_classe, eleve):
    classe = rechercher_classe(ecole, nom_classe)
    if classe is None:
        print("Classe introuvable")
        return False
    if rechercher_eleve(ecole, eleve.matricule)[1] is not None:
        print("Matricule déjà utilisé")
        return False
    classe.eleves.append(eleve)
    print("Élève ajouté en", classe.nom)
    return True


# ---------------------------------------------------------------
# FONCTION ajouter_note(ecole, matricule, matiere, valeur) : Booléen
# DEBUT
#     (c, e) <- rechercher_eleve(ecole, matricule)
#     SI e = NUL ALORS AFFICHER "Élève introuvable" ; RETOURNER Faux FIN SI
#     e.notes.ajouter( Note(matiere, valeur) )
#     RETOURNER Vrai
# FIN
# ---------------------------------------------------------------
def ajouter_note(ecole, matricule, matiere, valeur):
    classe, eleve = rechercher_eleve(ecole, matricule)
    if eleve is None:
        print("Élève introuvable")
        return False
    eleve.notes.append(Note(matiere, valeur))
    print("Note ajoutée")
    return True


# ---------------------------------------------------------------
# FONCTION moyenne_eleve(eleve) : Réel
# DEBUT
#     SI taille(eleve.notes) = 0 ALORS RETOURNER 0 FIN SI
#     somme <- 0
#     POUR chaque n DANS eleve.notes FAIRE
#         somme <- somme + n.valeur
#     FIN POUR
#     RETOURNER somme / taille(eleve.notes)
# FIN
# ---------------------------------------------------------------
def moyenne_eleve(eleve):
    if len(eleve.notes) == 0:
        return 0
    somme = 0
    for n in eleve.notes:
        somme = somme + n.valeur
    return somme / len(eleve.notes)


# ---------------------------------------------------------------
# PROCEDURE afficher_classe(classe)
# DEBUT
#     POUR chaque e DANS classe.eleves FAIRE
#         AFFICHER e.matricule, e.nom, e.prenoms, moyenne_eleve(e)
#     FIN POUR
#     AFFICHER "Effectif :", taille(classe.eleves)
# FIN
# ---------------------------------------------------------------
def afficher_classe(classe):
    print("--- Classe", classe.nom, "---")
    if len(classe.eleves) == 0:
        print("Aucun élève")
        return
    for e in classe.eleves:
        print(e.matricule, e.nom, e.prenoms, "| moyenne :", round(moyenne_eleve(e), 2))
    print("Effectif :", len(classe.eleves))


# ---------------------------------------------------------------
# FONCTION effectif_ecole(ecole) : Entier
# DEBUT
#     total <- 0
#     POUR chaque c DANS ecole.classes FAIRE
#         total <- total + taille(c.eleves)
#     FIN POUR
#     RETOURNER total
# FIN
# ---------------------------------------------------------------
def effectif_ecole(ecole):
    total = 0
    for c in ecole.classes:
        total = total + len(c.eleves)
    return total


# ---------------------------------------------------------------
# MENU : l'utilisateur saisit ses données
# ---------------------------------------------------------------
def main():
    while True:
        print("\n1-Ajouter classe  2-Ajouter élève  3-Ajouter note  4-Afficher classe")
        print("5-Chercher élève  6-Effectif de l'école  0-Quitter")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            ajouter_classe(ecole, input("Nom de la classe : "))
        elif choix == "2":
            nom_classe = input("Nom de la classe : ")
            matricule = input("Matricule : ")
            nom = input("Nom : ").upper()
            prenoms = input("Prénoms : ")
            ajouter_eleve(ecole, nom_classe, Eleve(matricule, nom, prenoms))
        elif choix == "3":
            matricule = input("Matricule de l'élève : ")
            matiere = input("Matière : ")
            valeur = float(input("Note sur 20 : "))
            ajouter_note(ecole, matricule, matiere, valeur)
        elif choix == "4":
            classe = rechercher_classe(ecole, input("Nom de la classe : "))
            if classe is None:
                print("Classe introuvable")
            else:
                afficher_classe(classe)
        elif choix == "5":
            classe, eleve = rechercher_eleve(ecole, input("Matricule : "))
            if eleve is None:
                print("Élève introuvable")
            else:
                print(eleve.nom, eleve.prenoms, "| classe", classe.nom,
                      "| moyenne :", round(moyenne_eleve(eleve), 2))
        elif choix == "6":
            print("Effectif de l'école :", effectif_ecole(ecole), "élèves")
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide")


main()