# Skriv ett program som visar en multiplikationstabell i ett rutnät.
# Programmet ska utformas så att man läser in antalet rader som ska skrivs ut.
# Använd nästlade for-satser.

# Läs in antalet rader för multiplikationstabellen
antal_rader = int(input("Ange antalet rader för multiplikationstabellen: "))

# Skapa multiplikationstabellen med nästlade for-loopar
for i in range(1, antal_rader + 1):
    for j in range(1, antal_rader + 1):
        # Beräkna produkten av i och j
        produkt = i * j
        # Skriv ut produkten med avstånd för att skapa ett rutnät
        print(f"{produkt:4}", end=" ")
    # Gör en ny rad efter varje rad i tabellen
    print()
