from collections import Counter 
 
def frq(str):
    cout = Counter(str)
    return cout
str = "sunny"
print(frq(str))