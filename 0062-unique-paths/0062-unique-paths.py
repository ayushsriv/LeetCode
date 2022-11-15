class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        spots = m+n-1
        numerator = denominator = 1
        
        for i in range(1,spots):
            numerator*=i
            
        for j in range(1,m):
            denominator*=j
        
        for k in range(1,n):
            denominator*=k
        
        return int(numerator/denominator)