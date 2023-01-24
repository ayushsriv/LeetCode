class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        num_dict = {}
        for i, val in enumerate(nums):
            num_dict[val]=i
        
        for j in range(len(nums)):
            for k in range(j+1,len(nums)):
                sum2 = (nums[j]+nums[k])*-1
                if sum2 in num_dict and num_dict[sum2]!=j and num_dict[sum2]>k:
                    res.add((nums[j],nums[k],sum2))
        
        return list(res)