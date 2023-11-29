# Skriv kundpris på en vara.
# Priset och momsen ska anges separat.

inköpspris = float(input('Ange varans inköpspris: '))

moms = inköpspris * 0.25

marknadspris = inköpspris + moms 

print (f'Marknadspriset för en vara är moms ({moms} kr) plus inköpspris ({inköpspris} kr), vilket ger kunden-priset {marknadspris} kr.')