def longest(s):
    prefix = s[0]
    for char in s[1:]:
        while not char.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == " ":
                return " "
    return prefix 
print(longest(["flow","flower","flesh"]))
