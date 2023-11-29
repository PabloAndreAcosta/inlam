# Skriv ett program som skriver ut en tabellför talen 1 till 12.
# På varje rad ska talet visas liksom talet i kvadrat och talet i kubik. 

print(                         )
print('  x-tal | x^2  |  x^3  ')
print('-----------------------')

for tal in range (1, 13):
    kvadrat = tal **2
    kubik = tal **3
    print(f'{tal:^5} | {kvadrat:^5} | {kubik:^7}')