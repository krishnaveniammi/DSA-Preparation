def paildrome(s):
    result = " "
    for char in s:
        if char.isalnum():
            char.lower()
            result +=char+result 
        return result == result[::-1]
s = "A man a plan a canal panama"
print(paildrome(s))
