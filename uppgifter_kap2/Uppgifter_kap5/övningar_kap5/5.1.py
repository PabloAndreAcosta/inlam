# Skriv ett program som läser in en mening bestående av mins två ord.
# Programmet ska sedan visa meddelande där det dels talarom hur många tecken användaren skrev och -
# visa vilket det första respektive sista ordet är.

text = input('Ange en text på minst två ord och extra blanka tecken: ')
words = text.split()

första_ordet = words [0]
sista_ordet = words [-1]

print(len(text))
print(första_ordet, sista_ordet)