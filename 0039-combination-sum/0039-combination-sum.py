class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(c,target+1):
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c])
            print(dp)
        return dp[-1]
        
        
        
        
#         def helper(res, tmp, candy, t):
#             if t < 0: return 
#             elif t == 0: 
#                 res.append(tmp) 
#                 return res
#             else:
#                 for i in range(len(candy)):
#                     helper(res, tmp+[candy[i]], candy[i:], t-candy[i])
#             print(res, tmp+[candy[i]], candy, t)
                
#         res = []
#         helper(res, [], candidates, target)    
#         return res
                