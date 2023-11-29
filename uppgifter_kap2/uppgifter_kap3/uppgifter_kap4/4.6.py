# Skriv ett program som beräknar summan (1/1-1/2)+(1/3-1/4)+(1/5-1/6) osv.
# Upprepningen ska savslutas när den sista termen man lagt till har ett absolutbelopp som är mindre än 0.000001.

summa = 0
n = 1

while True:
    term1 = 1/n
    term2 = 1/(n+1)
    summa += term1 - term2
    n += 2
    
    if abs(term1 - term2) < 0.000001:
        break

print(f"Summan är: {summa:.6f}")
