from is_prime import is_prime

n = int (input('Ange tal n'))
for i in range (2,n+1):
    if is_prime(i):
        print(i, end =', ')