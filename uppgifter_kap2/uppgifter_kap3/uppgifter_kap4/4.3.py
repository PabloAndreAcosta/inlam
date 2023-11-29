# Skriv ett program som räknar ut hur länge det tar innan man tjänat ihop 
# 10 miljoner om man tbänar 1 öre dag ett och sedan fördubblas lönen varje dag.

dagar = 0  # Initialt antal dagar
lön = 0.01  # Initial lön i ören

mål_belopp = 10000000  # 10 miljoner ören

while lön < mål_belopp:
    lönen_dubblas = lön * 2  # Fördubbla lönen
    lön = lönen_dubblas
    dagar += 1  # Öka antal dagar med 1

# Konvertera dagar till år och månader för att få en bättre uppfattning om tiden
år = dagar // 365
månader = (dagar % 365) // 30
dagar_restant = (dagar % 365) % 30

print(f"Det tar {år} år, {månader} månader och {dagar_restant} dagar att tjäna ihop 10 miljoner ören.")
