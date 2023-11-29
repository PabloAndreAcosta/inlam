# På ett matteprov kunde man få högst 50 poäng.
# Gränsen för betyget E är 25 poäng och för betygen D, C, B och A är 30, 35, 40 respektive 45 poäng.
#Skriv ett program som läser in poäng för en elev som visar vilket betyg hen fick på provet. 

# Elevens betyg. 
poäng = int(input('Ange poäng: '))

# Avgör bytgsgrad.
if poäng < 25:
    print ('Ditt betyg är F.')
elif poäng > 25 and poäng < 30:
    print ('Ditt betyg är E.')
elif poäng > 30 and poäng < 35:
    print ('Ditt betyg är D.')
elif poäng > 35 and poäng < 40:
    print ('Ditt betyg är C.')
elif poäng > 40 and poäng < 45:
    print ('Ditt betyg är B.')
else:
    print ('Ditt betyg är A.')