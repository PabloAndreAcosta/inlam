# Skriv ett program som beräknar kostnaden för att ringa med en mobiltelefon med ett abonemang. 
# Programmet ska läsa in hur många minuter man ringer per månad och hur mycket det kostar per minut. 
# Man får 10% rabbat om man ringer för 300 kr.

# Antal minuter per månad och kostnad per minut.
minuter = int(input('Ange antal minuter du ringer per månad: '))
pris = float(input('Ange pris per minut: '))

# Grundkostnad utan rabbat
kostnad = minuter * pris

# Kostnad med rabbat
rabatt = kostnad * 0.1

if kostnad < 300:
    print('Du har inte ringt tillräckligt för att få rabbat.')

elif kostnad > 300:
    kostnad -= rabatt
    print ('Du får 10 procent rabatt på din räkning.')
    
# Skriv ut den beräknade kostnaden
print (f'Den totala kostnaden för att ringa är {kostnad: .2f} kr.')
