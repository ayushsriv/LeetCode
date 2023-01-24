class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = nums[0]
        if maxi == 0 and len(nums)>1: return False
        for i in range(1,len(nums)):
            maxi = max(i+nums[i], maxi)
            if maxi==i and i!=len(nums)-1:
                return False
        return True
            