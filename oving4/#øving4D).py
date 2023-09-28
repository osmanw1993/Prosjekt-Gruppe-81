#øving 4d) 
#D) skal lage en funksjonen  som tar inn en liste med flytall  og en enkeltverdi , fra en txt fil
#funksjonen skal telle antall elementer i lista som er større enn eller like den oppgitte verdien og returnere dette tallet
def tell_elemnter_større_lik(list, verdi):
    
    tellinga = 0  # Initialize the count to 0.
    for num in list:  # Loop through each number in the list.
        if num >= verdi:  # If the number is greater than or equal to the given value,
            tellinga += 1 # increment the count by 1.
            # print(tellinga) 
    return tellinga

    
# Ex:
oppgitt_verdi= int(input("Skriv inn en verdi: "))
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
tell = tell_elemnter_større_lik(temperaturer, oppgitt_verdi)
print(f'The number of temperatures greater than or equal to {oppgitt_verdi} is: {tell}')