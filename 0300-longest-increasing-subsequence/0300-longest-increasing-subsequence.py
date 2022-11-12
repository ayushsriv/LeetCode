import numpy
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
            
        # maxlen = 1
        # for i in range(len(nums)):
        #     count = 1
        #     low = nums[i]
        #     for j in range(i, len(nums)):
        #         if nums[j]>low:
        #             low = nums[j]
        #             count += 1
        #         elif nums[j]>nums[i]:
        #             low = nums[j]
        #     maxlen = max(maxlen, count) 
        # return maxlen
 
