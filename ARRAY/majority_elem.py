def majority_elem(arr):
    count =0
    candidate = None 
    for i in arr:
        if count ==0:
            candidate = i
        count +=(1 if i ==candidate else -1)
    return candidate 
    
   
arr = [4,3,4]
print(majority_elem(arr)
