def count_vowels(str):
    vowels ="aeiouAEIOU"
    result = ""
    for i in str:
        if i not in  vowels:
            result += i
    return result

str = "sunny"
print(count_vowels(str))