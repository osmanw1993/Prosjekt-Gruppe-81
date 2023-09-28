#øving4g) 

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

# Ek:
x_liste = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
y_liste = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]

a, b = beregn_trend(x_liste, y_liste)
print(f"Trenden i datasettet er: verdi = {a}x + {b}")
