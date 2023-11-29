# Skriv ett program som beräknar hur många mil en bil har gått under det senaste året
# och bilens genomsnittliga bensinförbrukning per mil.
# När programmet körs ska det fråga efter dagens mätarställning, mätarställningen för ett år sedan
# och hur många liter bensin som har förbrukats under året.

import math 

Mätarställning_idag = float(input('Ange dagenns mätarställning: '))
Mätarställning_ett_år_sedan = float(input('Ange mätarställningen för ett år sedan: '))
Liter_bensin = float(input('Ange antal liter bensin som förbrukats: '))

Antal_körda_mil = Mätarställning_idag - Mätarställning_ett_år_sedan 
Förbrukning_per_mil =  Liter_bensin / Antal_körda_mil 

print(f'Antal körda mil är {Antal_körda_mil}')
print (f'Bensin förbrukningen per mil är {Förbrukning_per_mil: .2f} liter.')


