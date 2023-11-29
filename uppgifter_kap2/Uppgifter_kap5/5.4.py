# Leta efter det sista vita tecknet i texten.

s = input('Skriv en text: ')
i = 0   # i används som räknare
lenPaS = len(s)

for i in range (lenPaS -1, 0, -1):
  if s[i] == ' ':
    print(f'Visa mig {i}')
