# Skriv ett program som räknar ut det billigaste priset för ett kontantkort. Använd funktionen s.rpartition()


# Toma listor att förvara namn på kontantkorten och priser i.
namn = []
pris = []

# Oändlig loop som körs tills den avbryt när användaren trycker Enter utan att ange någon text.
while True:
    s = input('Namn och pris för ett kort: ')
    if s == '':
        break
    # Strängen s delas upp i tre delar där strängen delas upp vid ' ' somanges inom parentesen.
    namn_del, _, pris_del = s.rpartition(' ')
    # Här tars alla blanka tecken bort och resterande namnet till listan namn.
    namn.append(namn_del.strip())
    # listan pris konverteras till ett flyttal och läggs till listan pris.
    pris.append(float(pris_del))
# min(pris) används för att få priset med minst värde och sparas i variabeln m.
m = min(pris)
# Hitta index för lägsta pris i variabeln m och sparas i variabeln k.
k = pris.index(m)

# Skriver ut namnet på det billigaste abonemanget.
print(namn[k] + ' är billigast')
# Skriver ut kostnaden för det billigaste abonemanget. 
print(f'Kostnad: {m:1.2f} kr/månad')
