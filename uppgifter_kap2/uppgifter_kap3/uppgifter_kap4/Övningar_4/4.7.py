# Skriv ett program som visar en tabell med värden för uttrycket 2x**2-5x+1.
# Programmet ska skriva ut värdet av utrycket för x-värdena -10 till 10.

# Skapa en lista med x-värden från -10 till 10
x = list(range(-10, 11))

# Skriv ut rubriken för tabellen
print('                              ')
print('    x-värde | Uttryckets värde')
print('    -------------------------')

# Loopa igenom varje x-värde och beräkna uttryckets värde
for x in x :
    uttryck_värde = 2 * x**2 - 5 * x + 1
    print(f"{x:^15} | {uttryck_värde:^15}")
