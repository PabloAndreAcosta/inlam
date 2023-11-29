# Skriv ettt progam som läser in priset för ett årskort,
# priset för en biljett samt antalet gånger man planerar att besöka gymmet under ett år.
# Därefter ska progammet ange om det lönar sig att köpa årskort eller inte. 

# Ange biljett pris för enstaka besök, årskort samt antalbesök du täker göra på ett år.
årskort = int(input('Ange priset för ett årskort: '))
biljettpris = int(input('Ange biljettpris för drop in:'))
antal_besök = int(input('Ange antal besök per år: ')) 

# ange kostnaden för drop in samt årskort.
drop_in = antal_besök * biljettpris
årskort = årskort
# Beräkna om det lönar sig med årskort eller inte.
if  antal_besök * biljettpris < årskort:
    print ('Skaffa inte årskort, det är billigare att gå på drop in för dig.')
else:
    print('Du bör köpa årskort!')

# Angekostnaden kostnaden för drop in och för årskort. 
print (f'Kostnaden för drop in per år är {drop_in} kr. Kostnaden för årskort är {årskort} kr.')    