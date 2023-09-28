#øving4f)


#f)
#Find the length of the longest contiguous sequence of zeros in the list.

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


# Example usage:
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
length = longest_zero_sequence(dogn_nedbor)
print(f'The length of the longest contiguous sequence of zeros is: {length}')
