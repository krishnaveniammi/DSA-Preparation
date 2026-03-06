def arr_rotation(arr,k):
   k = k %len(arr)
   result = arr[-k:]+arr[:-k]
   return result
   
        
    
arr = [1,2,3,4,5,6,7]
print(arr_rotation(arr,3))
