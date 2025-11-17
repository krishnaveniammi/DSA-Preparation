def quik_sort(arr):
    if len(arr) <= 1 :
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >pivot]
    
    return quik_sort(left) + [pivot]+ quik_sort(right) 

print(quik_sort([3,6,8,10,1,2,1]))   