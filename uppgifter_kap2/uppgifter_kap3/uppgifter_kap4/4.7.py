# Skriv ett program som beräknar simhoppspoäng på detta sätt.
# Programmet ska först läsa in antalet domare och kontrollera att
# det är minst tre. Programmet ska utformas så att det sedan kan
# beräkna poäng för ett godtyckligt antal hopp. Varje ny beräkning
# ska inledas med att programmet läser in hoppets svårighetsgrad.
# Därefter ska domarpoängen läsas in. Det ska sedan beräkna och
# skriva ut hoppets poäng. Användaren ska kunna ange att programmet
# ska avslutas genom att skriva ett negativt tal vid någon inläsning.



# Funktion för att läsa in data.
def in_data():
   domare = int(input('Ange antal domare, ange minst tre st. '))

   while domare < 3:
        print('Du har angett för få domare, de måste vara minst tre stycken.')
        domare = int(input('Ange antal domare. '))

   return domare

# Funktion för att läsa process data.
def process(domare, svårighetsgrad):
    poäng = []

    for i in range (domare):
        poäng = int(input(f'Ange domare {i + 1} poäng mellan 1-10: '))
        domarpoäng = []

        domarpoäng.sort
        domarpoäng = domarpoäng [1:-1]
        medelvärde = sum(domarpoäng) / len(domarpoäng)

        hoppetspoäng = medelvärde * svårighetsgrad * 3

        return hoppetspoäng
    
# Funktion för att skriva utgående data.

def utdata(hoppetspoäng):
    print(f'Hoppetspoäng är: {hoppetspoäng:.2f}.')

# huvudprogram.    
def main ():
    