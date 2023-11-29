namn = 'fil.txt' # Filens namn.
text = '' # Tom sträng att lägga text i.
file = open(namn, 'r', encoding='utf-8') # Öppna fil för läsning.

text = file.read() # Läs fil.

file.close # Stäng fil.


print(text) # Skriv text.
print(text[0]) # Skriv först tkn i texten.
ord = text.split() # Split text.
print (ord [0]) # Skriv först ord i text. 