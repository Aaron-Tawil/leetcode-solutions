class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1 or nums[1]<nums[0]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        
        left, right = 0,n-1

        while left<right:
            mid = (left+right)//2
            if  nums[mid+1]>nums[mid]:
                left=mid+1
            elif mid-1>=0 and nums[mid-1]>nums[mid]:
                right = mid
            else:
                return mid
        return left # or right they should be equal here
        
        
        