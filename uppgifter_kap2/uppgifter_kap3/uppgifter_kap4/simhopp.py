# Skriv ett program som beräknar simhoppspoäng på detta sätt.
# Programmet ska först läsa in antalet domare och kontrollera att
# det är minst tre. Programmet ska utformas så att det sedan kan
# beräkna poäng för ett godtyckligt antal hopp. Varje ny beräkning
# ska inledas med att programmet läser in hoppets svårighetsgrad.
# Därefter ska domarpoängen läsas in. Det ska sedan beräkna och
# skriva ut hoppets poäng. Användaren ska kunna ange att programmet
# ska avslutas genom att skriva ett negativt tal vid någon inläsning.


# Funktion för att läsa indata
def indata():
    antal_domare = int(input("Ange antal domare (minst tre): "))
    
    while antal_domare < 3:
        print("Antalet domare måste vara minst tre.")
        antal_domare = int(input("Ange antal domare (minst tre): "))
    
    return antal_domare

# Funktion för att beräkna poäng
def process(antal_domare, svårighetsgrad):
    domarpoäng = []
    
    for i in range(antal_domare):
        poäng = float(input(f"Ange domare {i + 1}s poäng (0-10): "))
        domarpoäng.append(poäng)
    
    domarpoäng.sort()
    domarpoäng = domarpoäng[1:-1]  # Ta bort högsta och lägsta poängen
    medelvärde = sum(domarpoäng) / len(domarpoäng)
    
    hoppets_poäng = medelvärde * 3 * svårighetsgrad
    
    return hoppets_poäng

# Funktion för att skriva utdata
def utdata(hoppets_poäng):
    print(f"Hoppets poäng är: {hoppets_poäng:.2f}")

# Huvudprogram
def main():
    print("Simhoppspoängberäknare")
    
    while True:
        antal_domare = indata()
        if antal_domare < 0:
            break
        
        svårighetsgrad = float(input("Ange hoppets svårighetsgrad: "))
        if svårighetsgrad < 0:
            break
        
        hoppets_poäng = process(antal_domare, svårighetsgrad)
        utdata(hoppets_poäng)

if __name__ == "__main__":
    main()

