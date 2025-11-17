from collections import Counter 

def repeating_str(str):
    s = Counter(str)
    for key , value in s.items():
        if value > 1:
            print(key)
str = "sunnysu"
print(repeating_str(str))