#两数之和
#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
def two_sum(nums,target):
    length=len(nums)
    j=-1
    for i in range(length):
        if(target-nums[i]) in nums:
            if(nums.count(target-nums[i])==1 and nums[i]==target-nums[i]):
                continue
            else:
                j=nums.index(target-nums[i])
                break
    if j>0:
        return [i,j]
    else:
        return []
    
#字典模拟哈希表
def two_sum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]



