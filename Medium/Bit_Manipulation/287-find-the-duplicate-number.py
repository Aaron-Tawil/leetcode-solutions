class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast = nums[0]  
        fast = nums[fast]  
        slow = nums[0] 
        while slow!=fast:
            fast = nums[fast] 
            fast = nums[fast] 
            slow = nums[slow] 
        
        #now they supposed to be in the same position
        slow = 0
        while slow != fast:
            fast = nums[fast] 
            slow = nums[slow] 
        return slow
        