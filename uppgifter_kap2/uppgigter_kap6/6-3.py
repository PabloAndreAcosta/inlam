l = input ('Skriv en lista: ').split()
t = tuple(input('Skriv en tupel: ').split())

if l == t:
    print('Ska andlig hända')
l2 = list(t)
if l == l2:
    print('Lika')
else:
    print('Olika')