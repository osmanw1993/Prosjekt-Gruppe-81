#øving4M)
#Bruk funksjonen fra oppgave f) på den oppgitte lista «døgn-nedbør» for å finne den lengste perioden uten nedbør

def longest_zero_sequence(list):
    
    max_length = 0  # To store the maximum length of zero sequence
    current_length = 0  # To store the current length of zero sequence

    for num in list:  # Loop through each number in the list.
        if num == 0:  # If the number is zero,
            current_length += 1  # increment the current_length by 1.
            max_length = max(max_length, current_length)  # Update the max_length if current_length is greater.
        else:  # If the number is not zero,
            current_length = 0  # reset the current_length to 0.

    return max_length  # Return the maximum length of zero sequence.


dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
lengste_periode_uten_nedbør = longest_zero_sequence(dogn_nedbor)
print(f"Den lengste perioden uten nedbør er {lengste_periode_uten_nedbør} dager.")