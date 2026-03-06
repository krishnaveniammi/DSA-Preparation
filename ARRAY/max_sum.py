def max_sub_arr(arr):
   max_sum = arr[0]
   current = arr[0]
   for i in arr[1:]:
       current = max(i,current+1)
       max_sum = max(max_sum , current)
   return max_sum 
        
   
   
        
    
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_arr(arr))
