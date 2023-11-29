# Skriv ett proogram som beräknar hur många mil en bil har gått under det senaste året.
# Programmet ska beräkna den genomsnittliga bensin förbrukningen per mil. 

# Programmet ska fråga efter dagens mätarställning, mätarställningen för ett år sedan och hur många liter bensin–
# som förbrukats under året.



mätarställning_idag = float(input('Ange dagens mätarställning: '))
mätarställning_ettÅrSedan = float(input('Ange mätarställningen för ett år sedan: '))
liter_besin_som_förbrukats = float(input('Ange hur många liter bensin som förbrukats: '))

mil_senaste_året = mätarställning_idag - mätarställning_ettÅrSedan
liter_bensin_per_mil = liter_besin_som_förbrukats / mil_senaste_året

print(f'Bilen har gått {mil_senaste_året: .2f} mil och förbrukat {liter_bensin_per_mil: .2f} liter per mil.')