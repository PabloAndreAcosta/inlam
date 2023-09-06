
# En mobiloperatör erbjuder tre olika abonnemang: Kontant, Normal och Plus.

# Programmet ska läsa in hur många minuter man ptratar varje månad.
# Programmet ska berätta vilket abonnemang som lönar sig bäst beroende på hur mycket man ringer.
# Kontant är mest lönsamt om man ringer 33 minuter eller under.
# Normal lönar sig bäst om man ptar mellan 33 och 66 minuter. 
# Plus lönar sig bäst om man pratar mer än 66 minuter.

import math

minuter = int(input('Antal minuter per månad? '))
if minuter <= 33:
    print('Välj Kontant')
elif minuter > 33 and minuter <= 66:
    print('Välj Normal')
else:
    print('Välj Plus')    
