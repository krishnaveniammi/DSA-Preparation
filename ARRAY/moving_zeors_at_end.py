def moving_zeors(arr):
    for num in arr:
        if num == 0:
            arr.remove(num)
            arr.append(num)
    return arr
arr = [0,1,0,3,12]
print(moving_zeors(arr))
