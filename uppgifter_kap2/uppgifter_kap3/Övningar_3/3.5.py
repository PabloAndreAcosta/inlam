# Skriv ett program som läser in ett brevs längd, bredd och tjockek, 
# och som undersöker om brevet har tillåtna mått eller inte.
# Maximimått: Längd 600 mm, Tjocklek 100 mm, Bredd+längd+tjocklek högst 900 mm.
# Minimimått: Längd 140 mm, Bredd 90 mm.

längd = float(input('Ange längd: '))
bredd = float(input('Ange bredd: '))
tjocklek = float(input('Ange tjocklek: '))

if längd > 600 or längd < 140:
    print('Brevet är för långt eller kort.')
if bredd > 100 or bredd < 200:
    print('Brevet är för brett eller smalt.')
elif tjocklek > 100 or tjocklek < 90:
    print(' Brevet är för tjockt eller tunnt.')
