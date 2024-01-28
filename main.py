#main function
# Application 1
# Get user input
user_entered_phrase = input("Enter any words: ")

# Create a list of characters from the input
original_chars = list(user_entered_phrase)

# Create a list to hold the combined characters
combined_chars = [None] * (2 * len(original_chars))  

# Combine characters from the original list into alternating positions
combined_chars[::2] = original_chars  
combined_chars[1::2] = original_chars  

# Join the interleaved characters back into a string
combined_phrase = ''.join(combined_chars)

# Print the result
print(combined_phrase)


# Application 2
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Get user input for the letter range
user_range = input("Enter a range of letters (e.g., a-z): ")

# Extract start and end letters from the user input
start, end = user_range.split('-')

# Ensure both start and end letters are in lowercase
start = start.lower()
end = end.lower()

# Find the indices in the alphabet
start_index = alphabet.index(start)
end_index = alphabet.index(end)

# Create the result string by slicing the alphabet
result_string = alphabet[start_index:end_index + 1]

print(result_string)

