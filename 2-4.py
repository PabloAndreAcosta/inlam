# I USA brukar en bils bensinförbrukning anges i miles/gallon. 
# Skriv ett program som läser in en bensinförbrukning som är angiven på detta sätt och översätter den till det för oss vanligare liter/mil.
# Följande gäller 1 mile = 1.609 km och 1 gallon = 3.785 liter

miles_per_gallon = float(input('Ange bensinförbrukning i miles/gallon: '))

miles_to_km = 1.609
liter_per_gallon = 3.785
swedish_mile = miles_to_km * 10

liter_per_mile = (miles_per_gallon * liter_per_gallon) / swedish_mile

print(f'{miles_per_gallon} miles/gallon = {liter_per_mile: .3f} liter/mil')