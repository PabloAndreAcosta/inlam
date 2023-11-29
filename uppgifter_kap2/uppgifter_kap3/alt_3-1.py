
def abonemang (min):
 if min <= 33:
    utdata = 'Välj Kontant'
 elif min > 33 and min <= 66:
    utdata = 'Välj Normal'
 else:
    utdata = 'Välj Plus'
 return utdata

min = int(input('Antal minuter per månad? '))
print (abonemang(min))
