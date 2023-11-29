
# En mobiloperatör erbjuder tre olika abonnemang: Kontant, Normal och Plus.

# Programmet ska läsa in hur många minuter man ptratar varje månad.
# Programmet ska berätta vilket abonnemang som lönar sig bäst beroende på hur mycket man ringer.
# Kontant är mest lönsamt om man ringer 33 minuter eller under.
# Normal lönar sig bäst om man ptar mellan 33 och 66 minuter. 
# Plus lönar sig bäst om man pratar mer än 66 minuter.

import math

minuter_per_månad = int(input('Ange hur många minuter du pratar i genomsnitt verje månad: '))

if minuter_per_månad <= 33:
    print ('Kontantkort är ditt bästa val.')
elif minuter_per_månad > 33 and minuter_per_månad < 66:
    print ('Normal tycks vare rätt abonemang för dig.')
else:
    print ('Plus är rätt abonemang för dig.')




