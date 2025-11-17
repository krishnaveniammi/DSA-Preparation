def count_vowels(str):
    vowels ="aeiouAEIOU"
    cout_v = 0
    cout_c = 0
    for i in str:
        if i in vowels:
            cout_v +=1
        else :
            cout_c +=1
    return cout_v ,cout_c

str = "sunny"
print(count_vowels(str))