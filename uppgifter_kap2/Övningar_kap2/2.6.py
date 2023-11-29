# skriv ett program som läser in antal sekunder till en variabel med namnet tid.
# Indata till programmet ska vara ett helt antal sekunder, det vill säga ett heltal. 
# Programmet ska räkna om antalet sekunder så att jag kan uttryckas i timmar, minuter och sekunder.
# Där antalet minuter och sekunder ska ligga i intervallet noll till 59.
# Använd tre variabler: Tim, min och sek. 
# Skriv satsen som beräknar antalet timmar, minuter respektive sekunder och tilldela dessa världen till variablerna.

# Läs in antalet sekunder från användaren
tid = int(input('Ange sekunder du vill få i timmar, minuter och sekunder: '))
sekunder = tid

# Beräkna antalet timmar, minuter och sekunder

tim = sekunder / 3600 # Antal timmar (1 timme = 3600 sekunder)

sekunder_restant = sekunder % 3600 # Resten av sekunderna efter att timmarna har tagits bort

min = sekunder_restant / 60 # Antal minuter (1 minut = 60 sekunder)
sek = sekunder_restant % 60 # Resten av sekunderna

print(f'Tid anges i timmar {int(tim)}, minuter {int(min)} och sekunder {int(sek)}')