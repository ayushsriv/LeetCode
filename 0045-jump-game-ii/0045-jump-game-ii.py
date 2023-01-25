class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        dp = [float('inf')]*len(nums)
        
        for i in range(1,nums[0]+1):
            if i>=len(nums): break
            dp[i]=1
        
        for i in range(len(nums)):
            if dp[i]==float('inf'): continue
            for j in range(i+1,i+nums[i]+1):
                if j>=len(nums): break
                dp[j]= min(dp[i]+1,dp[j])
                        
        return int(dp[-1])