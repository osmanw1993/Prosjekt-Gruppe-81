#øving4k)
#Bruk funksjonen fra oppgave g) for å finne trenden i temperaturlista. For å finne trenden
#bruker dere lista «temperaturer_tidspunkter» som x-koordinater og lista «temperaturer»
#som y-koordinater. Skriv ut om trenden er stigende eller synkende. Trenden er stigende hvis
#a er positiv, synkende hvis a er negativ og det er ingen trend hvis a er 0.

def beregn_trend(x_liste, y_liste):
    #gjennomsnittet x-verdiene
    gjennomsnitt_x = sum(x_liste) / len(x_liste)
    
    # Beregn a ved formelen
    a_teller = sum((x - gjennomsnitt_x) * (y - sum(y_liste) / len(y_liste)) for x, y in zip(x_liste, y_liste))
    a_nevner = sum((x - gjennomsnitt_x) ** 2 for x in x_liste)
    a = a_teller / a_nevner
    
    # Beregn b ved formelen
    b = sum(y_liste) / len(y_liste) - a * gjennomsnitt_x
    
    return a, b

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)
 

a, b = beregn_trend(temperaturer_tidspunkter, temperaturer)

# Skriv ut trenden
if a > 0:
    trend = "stigende"
elif a < 0:
    trend = "synkende"
else:
    trend = "ingen trend (flat)"

print(f"Trenden i temperaturlisten er {trend}.")
