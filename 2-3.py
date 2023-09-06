# I Usa brukar man ange temperaturer i grader Fahrenheit (°F) istället för grader Celcius (°C). 
# 0°C motsvarar 32°F och 100°C motsvarar 212°F. 
# Man kan använda formeln °C =(°F-32)*5/9 för att omvandla från °F till °C.
# Skriv ett program som läser in  temperatur i Fahrenheit (°F) och omvandlar det till Celcius (°C).

fahrenheit = float(input('Ange grader i Fahrenheit: '))

celsius = (fahrenheit - 32) * 5/9

print(f'{int(fahrenheit)}°F motsvarar {int(celsius)}°C')