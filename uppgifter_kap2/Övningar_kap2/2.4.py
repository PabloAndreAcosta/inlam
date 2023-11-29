# Skriv ett program som läser in en kvadrats sida. Programmet ska beräkna omkrets samt area.

sida_av_en_kvadrat = int(input('Ange kvadratens längd: '))

x = sida_av_en_kvadrat

omkrets = x * 4

area = x **2

print (f'Kvadratens omkrets är {omkrets}')
print (f'Kvadratens area är {area}')