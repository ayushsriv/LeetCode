class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxArea = 0

        while i<j:
            Area = min(height[i], height[j])*(j-i)
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
            maxArea = max(maxArea, Area)

        return maxArea
    

