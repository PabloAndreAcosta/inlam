# I en triangel kan man beteckna sidorna med a, b och c. Om man känner till längderna för sidorna a och b
# samt vinkeln A kan man räkna ut c med formel c = math.sqrt((a**2 + b**2) (-2ab * math.cos(A))).
# Skriv ett Program som läser in längderna på två sidor i en triangel och vinken mellan sidorna.
# Programmet ska avgöra om triangeln är liksidig, likbent eller oliksidig.

import math
# Funktion för att avgöra triangeltypen
def Triangeltyp (a,b,A):
    # Beräkna sida c med folmel 
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(A)))

    # Jämför sidornas längder för att avgöra triangeltypen
    if a==b==c:
        return 'Liksidig triangel'
    elif a == b or a == c or b == c:
        return 'Likbent triangel'
    else:
        return 'Oliksidig triangel'

a = float(input('Ange a sidans länd: '))
b = float(input('Ange b sidans länd: '))
A = float(input('Ange vinkel: '))

# Anropa funktionen för att avgöra triangeltypen
resultat = Triangeltyp (a, b, A)

# Ange triangeltyp
print (f'Triangeln är {resultat}')
