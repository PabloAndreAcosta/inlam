# Beräkning av summa 1+2+3+ ... + n**2

n = int(input('Ange n? '))**2
summa = 0
k = 1
while k <= n:
    summa = summa + k   # Öka summan med k
    k = k + 1           # Öka k med 1
print('Summan blir', summa)

