# Skriv ett program som visar aktuellt datum och klockslag på följande sätt:
# dagens datum: åååå-mm-dd
# Klockan är: tt:mm:ss

import datetime

dt = datetime.datetime.now()

d = dt.date()
t = dt.time()
ttext = str(t) [0:8]

print(d)
print(ttext)