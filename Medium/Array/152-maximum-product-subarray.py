class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        #best sol
        # Initialize the global result with the first element or the max of the array
        res = max(nums)
        
        # curMax and curMin keep track of the products ending at the current position
        curMax, curMin = 1, 1
        
        for n in nums:
            # If we hit 0, we basically reset the streak
            # But our logic handles it by comparing with n (which is 0)
            
            # We store curMax in a temporary variable because it's used 
            # to calculate curMin in the next line
            tmp = curMax * n
            
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            # Update the overall maximum found so far
            res = max(res, curMax)
            
        return res



        #my solution...
        # n = len(nums)
        # if n==1:
        #     return nums[0]
        # pos = [0]*n
        # neg = [0]*n
        # for idx,num in enumerate(nums):
        #     if idx==0: #base case
        #         if num>0:
        #             pos[idx] = num
        #         else:
        #             neg[idx] = num    
        #     else:
        #         if num==0:
        #             pos[idx] = 0
        #             neg[idx]                                = 0
        #         elif num>0:
        #             pos[idx] = num*pos[idx-1] if pos[idx-1] else num
        #             neg[idx] = num*neg[idx-1] 
        #         else:
        #             pos[idx] = num*neg[idx-1] 
        #             neg[idx] = num*pos[idx-1] if pos[idx-1] else num
          
        # return max(pos)
   