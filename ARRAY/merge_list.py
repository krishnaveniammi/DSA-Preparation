def merge_list(arr1,arr2):
    arr1.extend(arr2)
    arr1.sort()
    n = len(arr1)
    mid = n//2
    return arr1[:mid],arr1[mid:]
arr1 = [1,3,5,7,9]
arr2 = [2,4,6,8,0]
print(merge_list(arr1,arr2))
