a = ' Erik Andersson 990314-2714  '

a = a.strip()
i = a.rfind(' ')+1
j = a.find('-')
b = a[i:j]

x = input('Ange Eriks födelsedatum, åå-mm-dd: ')

dag = a[19:21]
mån = a[17:19]

n = dag + '/' + mån

print(f'Eriks födelsedatum på N.Amerikanskt vis blir {n}.')