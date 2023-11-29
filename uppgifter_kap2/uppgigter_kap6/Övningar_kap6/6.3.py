# Skriv ett program som skapar en lista med 100 slumpmässiga heltal i intevallen 1 till 1000.
# Programmet ska sedan skriva ut det minsta och det största talen.
# Sam beräkna och skriva ut medelvärdet av den slumpmässiga listan.


import random

# Skapa en tom lista för att lagra slumpmässiga heltal
slumpmässiga_heltal = []

# Generera 100 slumpmässiga heltal och lägg till dem i listan
for i in range(100):
    slumpmässiga_heltal.append(random.randint(1, 1000)+1)

# Hitta det minsta och det största talet
minsta = min(slumpmässiga_heltal)
storsta = max(slumpmässiga_heltal)

# Beräkna medelvärdet
medelvarde = sum(slumpmässiga_heltal) / len(slumpmässiga_heltal)

# Skriv ut resultaten
print()
print("Slumpmässiga heltal i intervallet 1 till 1000:")
print()
print(slumpmässiga_heltal)
print()
print(f"Det minsta talet är: {minsta}")
print(f"Det största talet är: {storsta}")
print(f"Medelvärdet är: {medelvarde:.2f}")