def non_rep(str):
    n = len(str)
    for i in range (n):
        found = False
        for j in range(n):
            if i != j and str[i] == str[j]:
                found = True
        if not found:
            return str[i]
    return '$'
str = 'racecar'
print(non_rep(str))