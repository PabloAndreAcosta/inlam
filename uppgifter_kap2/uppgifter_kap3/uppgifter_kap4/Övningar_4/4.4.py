# Skriv ett program som beräknar hur många gånger en boll studsar, om bollen förlorar 30% studs vid varje studs,
# innan den blir still. 

höjd = int(input('Ange höjd i meter som en boll släpps från: '))

still = 0.01
studs = 0

while höjd > still:
    studs += 1
    höjd *= 0.7

print(f'Det tar {studs} antal studs innan bollen blir stillastående.')


