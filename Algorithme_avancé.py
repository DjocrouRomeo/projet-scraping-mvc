nom=input("Veillez entré votre nom : ")
matricule=input("veillez entré votre matricule : ")
moyenne=float(input("veillez entre=é votre moyenne : "))

if moyenne < 10 :
    print("L'étudiant"+nom+"est ajourné")

elif moyenne >= 10 and moyenne < 11 :
    print("L'étudiant"+nom+"a obtenue la mention passable")

elif moyenne >= 12 and moyenne >= 13:
    print("L'étudiant" + nom + "a obtenue la mention bien")

elif moyenne >= 14 and moyenne >= 15 :
    print("L'étudiant " + nom +  " a obtenue la mention très bien")

else:
    print("Erreur !")
