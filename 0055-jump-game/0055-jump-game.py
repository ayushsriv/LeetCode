class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0
        for i in range(len(nums)-1):
            maxi = max(i+nums[i], maxi)
            if maxi==i: return False
        return True
            