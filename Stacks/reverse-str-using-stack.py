def reverse_str(str):
    stack =[]
    result = ""
    for i in str:
        stack.append(i)
    for i in range(len(stack)):
        result +=stack.pop()
    return result 
print(reverse_str("ereredf"))
