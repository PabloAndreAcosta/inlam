konsonanter = 'bcdfghjklmnpqrstvxz'
rövarspråk = input('Skriv rövarspråk: ')
i = 0
while i < len(rövarspråk):
    print(s[i], end='')
    t = rövarspråk[i].lower()
    if t in konsonanter:
        i += 3
    else:
        i += 1