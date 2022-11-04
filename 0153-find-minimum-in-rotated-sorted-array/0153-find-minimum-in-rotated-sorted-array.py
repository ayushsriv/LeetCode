class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        mid = (low+high) // 2
        while low<high:
            if nums[low] < nums[high]:
                return nums[low]
            else:
                if nums[mid]<nums[high]:
                    high = mid
                else:
                    low = mid+1
            mid = (low+high) // 2
        return nums[low]
            
            
            