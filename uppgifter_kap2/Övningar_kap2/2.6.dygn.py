# Läs in antalet sekunder från användaren
tid = int(input('Ange sekunder du vill få i timmar, minuter och sekunder: '))
sekunder = tid
dygn = sekunder / 86400 # sekunder * minuter * timmar per dygn
# Beräkna antalet timmar, minuter och sekunder

tim = sekunder / 3600 # Antal timmar (1 timme = 3600 sekunder)

sekunder_restant = sekunder % 3600 # Resten av sekunderna efter att timmarna har tagits bort

min = sekunder_restant / 60 # Antal minuter (1 minut = 60 sekunder)
sek = sekunder_restant % 60 # Resten av sekunderna

print(f'Tid anges i dyn {int(dygn)}, timmar {int(tim)}, minuter {int(min)} och sekunder {int(sek)}')