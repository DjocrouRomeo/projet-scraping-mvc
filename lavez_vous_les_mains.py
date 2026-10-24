'''def Lavez_vous_les_mains():
    nbr_de_jours=int(input("Combien de fois vous vous lavez les mains par jours?: "))
    nbr_de_mois=int(input("durant combiens de mois que vous suivez cette routine?: "))
    jourstotaux=nbr_de_mois*30
    lavageTotaux=jourstotaux*nbr_de_jours
    secTotales=lavageTotaux*21
    nbr_minutes=secTotales//60
    nbr_secondes = secTotales % 60
    return f"{nbr_minutes} minutes et {nbr_secondes} secondes"
print("vous vous etes laver les mains durant",Lavez_vous_les_mains())'''


def wash_hands(n, Nm):
    ##n: Nombre de lavages par jour
    ##Nm: Nombre de mois
    SECONDES_PAR_LAVAGE = 21
    JOURS_PAR_MOIS = 30
    SECONDES= 60
    jours_total = Nm * JOURS_PAR_MOIS
    lavages_total = n * jours_total
    secondes_totales = lavages_total * SECONDES_PAR_LAVAGE
    minutes = secondes_totales // 60
    secondes = secondes_totales % 60
    return f"{minutes} minutes and {secondes} seconds"

print(wash_hands(8, 7))
print(wash_hands(0, 0))
print(wash_hands(7, 9))