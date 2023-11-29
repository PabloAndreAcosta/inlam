# Vid radioaktivt sönderfall kan man beräkna mängden kvarvarande radioaktivt material 'n' efter en viss tid 't' med formeln
# n = n₀e^(-λt)
# där n₀ är mängden radioaktivt material vid tiden t=0. Konstanten λ är en materialkonstant. 
# Man brukar för det mesta ange halveringstiden (den tid det tar innan hälften av det radioaktiva materialet sönderfallit).
# Om halveringstiden betecknas med T kan man räkna ut att: 
# λ = In(2)/T
# Halveringstiden för isotopen ¹⁴C är 5730 år. 
# Skriv ett program som skriver ut hur många procent av denna isotop som återstår efter S år. S ges som indata till programmet.

import math 

# Radioaktivt sönderfall - Formel: n = n₀e^(-λt)
# Radioaktivt material - 'n'
# Mängden raioaktivt material vid tiden t=0 - 'n₀'

# 'e' - Representerar det 10matematiska konstanta numret som kallas Euler's nummer(2.71828), som ofta betecknas som 'e'.
# math.exp() är en funktion för att beräkna eˣ 
# Exempel: 'eˣ = math.exp(x)

# Sönderfallskonstanten (λ) - Formel: 'λ = ln2 / T'
# 'λ' - Används för att beskriva hur snabbt något(i detta fall radioactiva material) försvinner
# In(x) - hur många gånger vi måste multiplicera ett nummer med sig själv för att få x.
# Exempel: 'In(2) = math.log(2)'
# 'T' - halveringstiden - Hur lång tid det tar för hälften av det radioaktiva materialet att försvinna.


# halveringstiden för Isotope ^14C
halfLifeC14 = 5730 

# Antal år programmet ska beräkna på
yearInput = float(input('Ange antal år: ')) 

# formeln 'λ = ln(2) / T'
theDecayConstant = math.log(2) / halfLifeC14 


# Beräkna hur många procent som återstår efter S år med formeln.
remainingIsotope= math.exp((-theDecayConstant) * yearInput) * 100 # * 100 för att få ut hur mycket av isotopen som är kvar i procent.

print(f'Efter {yearInput: .0f} år finns {remainingIsotope: .2f}% kvar av isotopen')

