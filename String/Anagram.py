def Anagram(s1,s2):
    return sorted(s1) == sorted(s2)
    
s1 = "nagram"
s2 ="nagram"
print(Anagram(s1,s2))
