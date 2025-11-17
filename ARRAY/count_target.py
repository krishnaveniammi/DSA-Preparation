def count_target(num ,target):
    cout =0
    for i in range(len(num)):
        if num[i] == target:
            cout +=1
    return cout
num = [1,2,3,1,2,5,7,1]
print(count_target(num,1))
