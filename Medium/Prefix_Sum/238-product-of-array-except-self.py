class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix  = [0]*n
        suffix = [0]*n
        for idx in range(n):
            if idx==0:
                suffix[n-idx-1] = 1
                prefix[idx] = 1
            else:
                suffix [n-idx-1 ] = suffix[n-idx]*nums[n-idx]
                prefix[idx] = prefix[idx-1]*nums[idx-1]

        return [ prefix[i] * suffix [i] for i in range(n)] 
        