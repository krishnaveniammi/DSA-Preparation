def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)-2):
        l = i+1
        r = len(nums)-1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s == 0:
                result.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1

    return result

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
