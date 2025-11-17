import re   

def remove_special_characters(input_string):
    # Remove all characters except alphabets, numbers, and spaces
    return re.sub(r'[^A-Za-z0-9 ]+', '', input_string)

# Example usage
user_input = input("Enter a string: ")
cleaned = remove_special_characters(user_input)
print("String after removing special characters:", cleaned)
