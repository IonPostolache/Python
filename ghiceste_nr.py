# imprumutam cod extern, ca sa nu mai reinventam noi logica
import random

# generam un numar aleatoriu intre 0 si 30
numar_secret = random.randint(0, 30)
# setam numarul ghicit cu o valoare gresita
numar_ghicit = -1

# atat timp cat numarul ghicit e diferit de numarul secret jocul incepe/continua
while numar_ghicit != numar_secret: # != verifica daca stanga e diferita de dreapta
    # luam de la tastatura o valoare si o transformam in nr intreg
    numar_ghicit = int(input("ghiceste un numar intre 0 si 30 \n"))
    # scriem logica pentru cele 3 cazuri posibile
    if numar_secret > numar_ghicit:
        print("Numarul secret e mai mare")
    elif numar_secret < numar_ghicit:
        print("Numarul secret e mai mic")
    else:
        print("Felicitari!!!")
