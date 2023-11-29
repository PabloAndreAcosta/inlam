s = input('Ange en text: ')
n = 0

for i in range (0, len(s) -1, 1):
     if s[i] == ' ' or s[i] == '\t':
        n = i
        break
     
print(f'Första blanka finns på index {n}.')
    