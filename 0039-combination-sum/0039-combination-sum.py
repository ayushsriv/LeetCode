class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(res, tmp, candy, t):
            if t < 0: return 
            elif t == 0: 
                res.append(tmp) 
                return res
            else:
                for i in range(len(candy)):
                    helper(res, tmp+[candy[i]], candy[i:], t-candy[i])
            print(res, tmp+[candy[i]], candy, t)
                
        res = []
        helper(res, [], candidates, target)    
        return res
                