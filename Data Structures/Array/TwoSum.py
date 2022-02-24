def TwoSum(nums,target):
    d={}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]],i]
        else:
            d[nums[i]]=i

nums=list(map(int,input().split()))
target=int(input())
result=TwoSum(nums,target)
print(result)