def extract_digits(str):
    result = []
    for i in str:
        if i.isdigit():
            result.append(int(i))
    return result
            
str = "123dsaw2"
print(extract_digits(str))
