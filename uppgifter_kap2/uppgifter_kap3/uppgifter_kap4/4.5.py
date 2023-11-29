# En kommun har gjort följande prognos för befolkningsutvecklingen de närmsta åren.
# Vid början av år 2022 hade kommunen 26000 invånare.
# Antal födda och avlidna under ett år uppskattas vara 0,7% respektive 0,6% av befolkningen vid årets början.
# Antalet inflyttade och antalet utflyttade uppskattas till 300 respektive 325 varje år.
# Skriv ett program som beräknar kommunens uppskatade invånarantal i början av ett visst år.
# Vilket år det gäller ska läsas indata till programmet. 

# Läs in årtalet från användaren
år = int(input("Ange årtalet: "))

# Startvärden
befolkning = 26000  # Befolkningen vid början av 2022
fodselprocent = 0.007  # 0,7% födda per år
dodsprocent = 0.006  # 0,6% avlidna per år
inflyttade = 300
utflyttade = 325

# Beräkna befolkningen för varje år fram till det angivna året
for i in range(2022, år):
    fodelse = befolkning * fodselprocent
    död = befolkning * dodsprocent
    befolkning += fodelse - död + inflyttade - utflyttade

# Skriv ut det uppskattade invånarantalet för det angivna året
print(f"Det uppskattade invånarantalet i början av år {år} är {int(befolkning)}.")
