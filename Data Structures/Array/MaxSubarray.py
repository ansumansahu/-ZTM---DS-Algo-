def maxSubArray(nums):
    max_sum=nums[0]
    max_nums=nums[0]
    for i in range(1,len(nums)):
        max_nums=max(nums[i],max_nums+nums[i])
        max_sum=max(max_nums,max_sum)
    return max_sum

nums=list(map(int,input().split()))
result=maxSubArray(nums)
print(result)