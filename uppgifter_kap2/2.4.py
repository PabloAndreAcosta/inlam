# I USA brukar en bils bensinförbrukning anges i miles/gallon. 
# Skriv ett program som läser in en bensinförbrukning i miles per gallon och -
# översätter miles/gallon till det för oss vanligare liter/mil.
# Följande gäller 1 mile = 1.609 km och 1 gallon = 3.785 liter

miles_per_gallon = float(input('Ange bensinförbrukning i mile/ gallon: '))
km_per_mile = 1.609 
liter_per_gallon = 3.785
svenska_mil = km_per_mile  * 10

liter_per_mil = (miles_per_gallon * liter_per_gallon) / svenska_mil

print (f'{miles_per_gallon} mile per gallon är lika med {liter_per_mil: .3f} liter per mil')
