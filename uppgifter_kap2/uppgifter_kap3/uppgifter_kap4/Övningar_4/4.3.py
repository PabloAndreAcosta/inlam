# Skriv ett program som läser in ett  heltal n och beräknar den harmoniska serien. Dvs 1/1 + 1/2 + 1/3 + .... + 1/n.

n = int(input('Ange n. '))
summan = 0
k = 1/n
while k <= n:
    summan = summan + k
    k = k + 1
print ('Summan blir', summan)
