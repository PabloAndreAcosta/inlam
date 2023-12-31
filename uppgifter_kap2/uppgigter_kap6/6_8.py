# Sevdo. Start ---> Antal prov -----> Skapa en tom lista Prov -----> Skapa en tom lista Namn.

antal_prov = int(input('Anttal prov? '))
print('Avsluta med en tom rad.')
namn = []
poäng = []
while True:
    s = input('Namn? ')
    if s == '':
        break
    namn.append(s)
    s = input('Poäng? ')
    if s == '':
        break
    ls = s.split()
    p = [float(e) for e in ls]
    if len (p) == antal_prov:
        poäng.append(p)
    else:
        print('Felaktig antal reultat. ')
        namn.pop()    # Ta bort elever
n = len(namn)   # Antal elever

# Beräkna genomsnitt för varje elev
for k in range (0, n):
    g = sum(poäng[k])/antal_prov
    print(f'Genomsnittspoäng för {namn[k]}: {g:.1f}')

# Beräkna genomsnitt för varje prov.
for i in range(0, antal_prov):
    summan = 0;
    for j in range(0, n):
        summan += poäng[j][i]
    print(f'Genomsnittspoäng på prov nr {i+1}: {summan/n:.1f}')    