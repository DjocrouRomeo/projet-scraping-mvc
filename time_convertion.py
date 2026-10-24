import time
def convertion():
    global secondes, minute
    while True:
        try:
            minute=int(input("Saisissez le nombre de minutes: "))
        except ValueError:
            input("Veillez obligatoirement saisir une valeur correcte:")
        else:
            secondes= int(minute) * 60
        if secondes==0 or minute==0:
            print(f"{minute}minute={secondes}seconde")
        else:
            print(f"{minute}minutes={secondes}secondes")
            break

convertion()