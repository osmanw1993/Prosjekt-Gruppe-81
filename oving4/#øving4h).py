#øving4h)
#Anta du har en plante som krever at temperaturen er +5 grader celsius for å vokse i det hele
#tatt, og så vokser fortere desto varmere det er, lineært med temperatur over 5 grader. Skriv
#en funksjon som regner ut summen av alle tall over 5 i lista

def plantvekst(tempListe):

    total_vekst = 0

    for temperatur in tempListe:
        if temperatur > 5:
            vekst = temperatur - 5 
            total_vekst += vekst 

    return total_vekst


 
# eks:
tempListe = [4, 7, 15]
resultat = plantvekst(tempListe)
print(resultat)

def beregn_summen(liste):
    total_sum = 0
    
    for tall in liste:
        if tall > 5:
            differanse = tall - 5
            total_sum += differanse
    
    return total_sum

# Eksempel:
liste = [4, 7, 15]
resultat = beregn_summen(liste)
print(resultat)  # Dette vil skrive ut 12 (0 + 2 + 10)


