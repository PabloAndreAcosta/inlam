# Skriv ett program som läser in ett antal heltal och som skriver ut dem i samma ordning som de lästes in. 
# Vid utskriften ska ett visst tal skrivas ut bara en gång. 

s = input('Skriv ett antal heltal: ') # tar in tal
ls = s.split() # tar bort mellanrum i början och slutet
tal = [int (e) for e in ls]
for i in range (0, len(tal)):
    if not tal[i] in tal[0:i]:
       print (tal[i], end=' ')
