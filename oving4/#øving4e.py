#øving4e
#Skriv en funksjon som tar inn ei liste med tall. For hvert tall i lista unntatt det siste skal
#funksjonen regne ut differansen mellom neste tall i lista og dette tallet. Differansene skal
#legges inn i ei ny liste

def calculate_differences(list):
    
    differences = []  # Initialize an empty list to store the differences.
    for i in range(len(list) - 1):  # Loop through the list up to the second-last element.
        diff = list[i + 1] - list[i]  # Calculate the difference between the next number and the current number.
        differences.append(diff)  # Add the difference to the 'differences' list.
    return differences  # Return the list of differences.


# Ex:
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
differences = calculate_differences(temperaturer)
print(f'The differences between temperatures are: {differences}')
