'''
WHILE
se evalueaza o singura conditie
atat timp cat conditia este adevarata, se executa codul aferent acesteia
ex:
atat timp cat inca ploua:
    'tin umbrela deasupra capului'
'''
"""
benzina_ramasa = 7
while benzina_ramasa > 0:
    # accelerez
    print('Vruum Vruum!')
    # in timp ce accelerez se consuma un l de benzina
    benzina_ramasa = benzina_ramasa - 1
    # se pot intercala alte notiuni invatate
    # daca mai avem doar 1 l, atentionam soferul
    if benzina_ramasa == 1: # == este operator de comparare
        print('Atentie! Mai ai doar 1 l de benzina')

print('Stop! Ai ramas fara benzina')
"""
'''
exercitiu:
super mario are 3 vieti
atat timp cat mai are vieti, te poti juca (print start game)
incepe jocul si mario pierde cate o viata
optional poti printa ('Ai pierdut o viata. Mai ai x vieti')
la final printeaza 'game over'
'''

vieti_ramase=3
print("Start game!")
print(f"Ai {vieti_ramase} vieti.")
while vieti_ramase>0:
    #print(f"Mai ai {vieti_ramase} vieti")
    vieti_ramase=vieti_ramase-1
    print(f"Ai pierdut o viata. Mai ai {vieti_ramase} vieti.")

print("Game over!")



