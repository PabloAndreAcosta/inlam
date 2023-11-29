
# In data. Text fil hämtad från GitHub AIDEV23S.
text = 'Välkommen till boken Python från början! Detta är boken för dig som vill lära dig att programera  i Python. Du begöver inte ha några tidigare kunskaper i programmering, men det är bra om du är van att använda datorer.'

# Tom sträng som kommer hålla den översatta texten.
rövarspråk = ''
konsonant = 'BCDFGHJKLMNPQRSTVXZbcdfghjklmnpqrstvxz'

# Här gör vi texten läsbar och lite snygg.
#text = text.capitalize()

# Här kör jag en loop som stegar genom alla index i strängen. Om index är en konsonant läggs den in i strängen
# med en ett 'o' följt av en till konsonant. Annars, om det är en vokal, lägs bara vokalen in i index i stängen.
for i in text:
    if i in konsonant:
        rövarspråk += i + 'o' + i
    else:
        rövarspråk += i 

# Här skrivs personens text ut.        
print(f'Här är din text i rövarspråk: ' + rövarspråk)



