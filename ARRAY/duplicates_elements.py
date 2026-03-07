def duplicates_arr(arr):
    seen = set()
    dup =[]
    for num in arr:
        if num in seen:
            dup.append(num)
        else:
            seen.add(num)
    return dup
arr = [4,3,2,7,8,2,3,1]
print(duplicates_arr(arr))
