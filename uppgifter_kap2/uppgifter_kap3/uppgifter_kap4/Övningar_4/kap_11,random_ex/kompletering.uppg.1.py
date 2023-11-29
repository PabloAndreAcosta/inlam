
# Här hämtar jag filen.
namn = '/Users/PabloAcosta/Downloads/svenskt_text.txt' # Filens namn.
text = '' # Tom sträng att lägga text i.
file = open(namn, 'r', encoding='utf-8') # Öppna fil för läsning.
text = file.read() # Läs fil.
file.close # Stäng fil.

# Tom sträng som kommer hålla den översatta texten.
rövarspråk = ''
konsonant = 'BCDFGHJKLMNPQRSTVXZbcdfghjklmnpqrstvxz'

# Här gör vi texten läsbar och lite snygg.
text = text.capitalize()

# Här kör jag en loop som stegar genom alla index i strängen. Om index är en konsonant läggs den in i strängen
# med en ett 'o' följt av en till konsonant. Annars, om det är en vokal, lägs bara vokalen in i index i stängen.
for i in text:
    if i in konsonant:
        rövarspråk += i + 'o' + i
    else:
        rövarspråk += i 

# Här skrivs personens text ut.        
print(f'Här är din text i rövarspråk: ' + rövarspråk)

