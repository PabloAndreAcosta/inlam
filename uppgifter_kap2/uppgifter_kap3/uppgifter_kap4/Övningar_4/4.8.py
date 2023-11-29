# Skapa en lista med x-värden från -1 till 1
x = list(range(-10, 11))

# Skriv ut rubriken för tabellen
print('                              ')
print('x-värde | Uttryckets värde')
print('-------------------------')

# Loopa igenom varje x-värde och beräkna uttryckets värde
for x in x :
    x = x / 10
    uttryck_värde = 2 * x**2 - 5 * x + 1
    print(f"{x:^7} | {uttryck_värde:^15.3f}")