class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (high+low)//2
            if nums[mid]<=nums[mid-1] and nums[mid]<=nums[mid+1]:
                return nums[mid]
            elif nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid-1
        return nums[high]
            
            
            
            