#øving4J)
#Bruk funksjonen fra oppgave e) til å finne ut om temperaturen er stigende eller synkende for
#hvert tidspunkt. Gå gjennom lista som dere får når dere kaller funksjonen fra oppgave e) på
#temperaturlista. For hvert element skriv ut indeksen og skriv ut «stigende» om differansen er
#over 0, «synkende» om den er negativ eller «uforandret» om den er 0.

def calculate_differences(list):
    
    differences = []  
    for i in range(len(list) - 1):  
        diff = list[i + 1] - list[i]  
        differences.append(diff)  
    return differences  


def determine_trend(list):
    differences = calculate_differences(list)
    trends = []
    
    for diff in differences:
        if diff > 0:
            trend = "stigende"
        elif diff < 0:
            trend = "synkende"
        else:
            trend = "uforandret"
        trends.append(trend)
    
    return trends

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
temperature_trends = determine_trend(temperaturer)

for i, trend in enumerate(temperature_trends):
    print(f"Indeks {i}: Temperaturtrend er {trend}")




