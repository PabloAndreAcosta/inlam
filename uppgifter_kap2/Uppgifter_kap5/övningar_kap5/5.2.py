# skriv ett program som läser in ett personnummer och skriver ut meddelandet: Grattis! ( Om den aktuella personen fyller år)
# personnumret anges med tio siffror utan bindesträck.

import datetime

person_nr = input('Ange ditt personnummer med tio siffror utan bindesträck: ')

if len(person_nr) != 10: 
    print('Ogiltigt personnummer!')

år = int(person_nr[:2])
mån = int(person_nr[2:4])
dag = int(person_nr[4:6])
    
idag = datetime.date.today()

if idag.day == dag and idag.month == mån:
    print('Grattis MOFO!')
else:
    print('Inte din dag idag.')


