t = float(input('Ange temperatur: '))
if t < 18:
    print('Det är kallt.')
    print('Sätt på värmen.')
    if t < 12:
        print('Och jackan.')
    if t <= 10:
        print('Det är svinkallt, börja göra burpees.')    
else:
    print('Det är varmt.')
    if t >= 22:
        print('Stäng av värmen.')
    if t >= 30:
        print('Dags att gå ut och sola.')    
print(f'Det är {t:.1f} grader.')