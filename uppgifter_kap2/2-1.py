# Skriv ett program som beräknar hur många mil en bil har gått under det senaste året
# och bilens genomsnittliga bensinförbrukning per mil.
# När programmet körs ska det fråga efter dagens mätarställning, mätarställningen för ett år sedan
# och hur många liter bensin som har förbrukats under året.


metersettings_today = float(input('Mätarställning idag? '))
metersettings_a_year_ago = float(input('Mätarställnig för ett år sedan? '))
driven_miles = metersettings_today - metersettings_a_year_ago
gas_consumption = float(input('Antal liter bensin förbrukat: '))

consumption_per_mile = gas_consumption / driven_miles
print(type(consumption_per_mile))

print(f'Förbrukning per mil: {consumption_per_mile: .2f}')
