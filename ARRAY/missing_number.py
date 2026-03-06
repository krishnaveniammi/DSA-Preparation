def missing_num(arr ,n):
   total = n*(n+1)//2
   return total- sum(arr)

arr = [1, 2,4,5,6]
n = 6
print(missing_num(arr,n))
