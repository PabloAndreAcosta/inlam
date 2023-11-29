# Skriv ett program som läser inn ett godtyckligt antal heltal. 
# Programmet ska undersöka hur många av de inlästa talen som r mindre än noll.


heltal = input('Ange några heltal: ')
Heltalslista = heltal.split()

heltalen = [int(tal) for tal in Heltalslista if int(tal) > 0]

print(heltalen)
       
      
