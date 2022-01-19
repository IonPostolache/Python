'''
IF ELSE
se evalueaza rand pe rand conditii, de sus in jos
cand se gaseste una Adevarata, se executa codul corespunzator acesteia
'''

cc = 2400
if cc < 50: # un sg if la inceput (obligatoriu)
    print('motocicleta: impozit 70 lei')
elif cc < 2000: # putem pune oricate elif (optionale)
    print('masina mica: impozit 160 lei')
else: # un sg else la final (optional)
    print('suv: impozit 900 lei')

ora=8
if ora<12:
    print("buna dimineata")
elif ora<18:
    print("buna ziua")
else:
    print("buna seara")
'''
exercitiu: robotel care ne saluta la intrarea unui hotel, in f de ora 
daca ora e < 12 => buna dimineata
daca ora e < 18 => buna ziua
altfel => buna seara
'''