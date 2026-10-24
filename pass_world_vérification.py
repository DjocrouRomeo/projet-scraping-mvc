Listes_des_MDP=[123456,"password","azerty","admin","letmein","qwerty"]
enumerate(Listes_des_MDP)
print(Listes_des_MDP)
for index , mdp in enumerate(Listes_des_MDP, start=1):
    print(f"{index} : {mdp}")
MDP=input("Veuillez saisir un Mots de passe : ")
if MDP in Listes_des_MDP:
    print("Ce mots de passe est très faible ")
else:
    print(" Pas dans la liste des plus faibles ")