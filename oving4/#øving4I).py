#øving4I)

#Bruk funksjonen fra oppgave d) på lista «temperaturer» fra fila. Anta at hvert innslag er
#maksimaltemperaturen for en dag. Finn antall sommerdager (over 20), høysommerdager
#(over 25) og tropedager (over 30).

def tell_elemnter_større_lik(list, verdi):
    
    tellinga = 0  # Initialize the count to 0.
    for num in list:  # Loop through each number in the list.
        if num >= verdi:  # If the number is greater than or equal to the given value,
            tellinga += 1  # increment the count by 1.
    return tellinga

    

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
antall_sommerdager = tell_elemnter_større_lik(temperaturer, 20)
antall_hoysommerdager = tell_elemnter_større_lik(temperaturer, 25)
antall_tropedager = tell_elemnter_større_lik(temperaturer, 30)
print("Antall sommerdager (over 20 grader):", antall_sommerdager)
print("Antall høysommerdager (over 25 grader):", antall_hoysommerdager)
print("Antall tropedager (over 30 grader):", antall_tropedager)