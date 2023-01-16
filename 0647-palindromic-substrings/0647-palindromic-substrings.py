class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(1,len(s)):
            def helper(l, h):
                res = 0
                for j in range(len(s)): 
                    low = l-j
                    high = h+j
                    if low<0 or high>len(s)-1:
                        break
                    if s[low]==s[high]:
                        res+=1
                    else:
                        break
                return res
            res += helper(i-1,i)
            res += helper(i,i)
        return res+1            
