# Skriv ett program som undersöker om en texts första och sista tecken är samma.

text = input("Ange en text: ")

if text [-1] == text [0]:
    print("Första och sista tecknet är samma i texten.")
else:
    print("Första och sista tecknet är olika i texten.")