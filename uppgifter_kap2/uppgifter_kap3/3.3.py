# Skriv ett program som läser två sidor på en triangel och vinkeln mellan sidorna.
# programmet ska avgöra om triangeln är Liksidig, Likbent eller oliksidig.
# Formeln c = math.sqrt (a **2 + b **2)- (2ab * math.cosA)

import math

a = float(input('Ange tringelsida a: '))
b = float(input('Ange triangelsida b: '))
A = int(input('Ange triangelvinkel A: '))

c = math.sqrt (a **2 + b **2)- (2*a*b * math.cos(A))

if a == b and b == c:
    print ('Triangeln är liksidig.')
elif a == b:
    print ('Tringeln är likbent.')
else:
    print ('triangeln är oliksidig.')