def count_word_largest():
    s1 = "this is sunnyt go"
    s = s1.split()
    longest_length = 0
    longest_word = ""  # Initialize to store the actual word

    for i in s:
        if len(i) > longest_length:
            longest_length = len(i)
            longest_word = i  # Update the longest word

    # Return the length of the longest word, or the word itself
    return longest_length 
    # To return the word itself, use: return longest_word
    # To return both, use: return longest_word, longest_length

# Call the function and print the result
length = count_word_largest()
print(f"The length of the longest word is: {length}") 
