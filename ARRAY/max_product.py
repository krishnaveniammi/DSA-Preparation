def max_product(nums):
    max_p = min_p = result = nums[0]

    for i in nums[1:]:
        temp = max(i, max_p*i, min_p*i)
        min_p = min(i, max_p*i, min_p*i)
        max_p = temp

        result = max(result, max_p)

    return result

arr = [2,3,-2,4]
print(max_product(arr))
