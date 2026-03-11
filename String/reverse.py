def reverse(s):
    result = " "
    for char in s:
        result = char + result
    return result 
s = "sunny is bad girl"
print(reverse(s))
