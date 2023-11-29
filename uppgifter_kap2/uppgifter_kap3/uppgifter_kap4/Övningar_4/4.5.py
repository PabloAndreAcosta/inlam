# Skriv ett program som beräknar hur många gånger en boll studsar, om bollen förlorar 30% studs vid varje studs,
# innan den blir still. 
# Man ska göra upprepade beräkningar där bollen släpps från olika höjder.
# Programmet ska avslutas när ett negativt tal skrivs in. 

while True:
# Ange höjden bollen släpps från. Samt att koden ska avbrytas när det är talet blir noll eller negativt. 
  höjd = int(input('Ange höjd, i meter, som en boll släpps från: '))
  if höjd <= 0:
    break
# Ange parametrar bollens vriabler, stillhet och studs. Bollens studs agerar räknare. 
  still = 0.01
  studs = 0
# Ger förutsättningar för logoska uttyck och satser.
  while höjd > still:
    studs += 1
    höjd *= 0.7
# Skriver resultatet när koden avbryts. 
print(f'Det tar {studs} antal studs innan bollen blir stillastående.')


