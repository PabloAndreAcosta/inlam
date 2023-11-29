# I en geometrisk talföljd får man ett tal i följden genom att multiplicera det föregående talet med en viss konstant k.
# Skriv ett program som konstruerar en geometrisk talföljd där konstanten k är lika med 3 och det första talet i följden är 2.
# Talföljden ska läggs i en lista som ska skrivs ut. Låt den som kör programmet bestämma hur många tal som ska tas med i listan. 

n = int(input('Hur många tal önskas? '))
k = 3
a = 2
talföljd = [a]
for i in range(1, n):
    a *= k
    talföljd.append(a)

print(talföljd)
