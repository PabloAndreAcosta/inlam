# Skriv ett program som beräknar hur många mil en bil har gått under det senaste året
# och bilens genomsnittliga bensinförbrukning per mil.
# När programmet körs ska det fråga efter dagens mätarställning, mätarställningen för ett år sedan
# och hur många liter bensin som har förbrukats under året.

import math 

mätarställning_idag = float(input('Mätarställning idag? '))
mätarställning_ett_år_sedan = float(input('Mätarställning för ett år sedan? '))

körda_mil = mätarställning_idag - mätarställning_ett_år_sedan

print(f'Antal körda mil: {körda_mil}')

bensin_förbrukning = float(input('Antal liter bensin förbrukat: '))
förbrukning_per_mile = bensin_förbrukning / körda_mil

print(f'Förbrukning per mil: {förbrukning_per_mile:.2f}')
