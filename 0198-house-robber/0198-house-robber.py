class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        n2 = nums[0]
        n1 = max(nums[:2])
        for i in range(2,len(nums)):
            n2,n1 = n1,max(nums[i]+n2,n1)

        return n1