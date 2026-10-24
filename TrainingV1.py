def SommeNbrPaire(Liste_A, Liste_B):
    liste_A=[1,2,3,4,5]
    liste_B=[10,23,36,47]
    for p in liste_A:
        if p % 2 == 0:
            SmmPaire1= p*p
            print(SmmPaire1)
    for s in liste_B:
        if s % 2 == 0:
            SmmPaire2 = s * s
            print(SmmPaire2)
    return print(SmmPaire1), print(SmmPaire2) 

