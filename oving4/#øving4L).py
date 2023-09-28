#øving4L)
#Bruk funksjonen fra oppgave h) for å finne total vekst for planten gitt lista med temperaturer

def plantvekst(tempListe):

    total_vekst = 0

    for temperatur in tempListe:
        if temperatur > 5:
            vekst = temperatur - 5 
            total_vekst += vekst 

    return total_vekst

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
total_vekst = plantvekst(temperaturer)

print(f"Total vekst for planten basert på temperaturene er {total_vekst}.")