# Skriv ett program som läser in ett personnummer och avgör om det är en man eller kvinna.

import datetime

personnummer = input('Ange ditt personnummer, 10 siffror utan bindesträck: ')

if len(personnummer) != 10:
    print('Ogiltigt personnummer.')

else:
    man_eller_kvinna = int(personnummer[-2])


if man_eller_kvinna % 2 == 0:
    print('Detta är en kvinna.')

else:
    print('Detta är en man.')
