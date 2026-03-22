class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0 
        l,r = 0,n-1
        while l<r:
            curr = (r-l) * min(height[l],height[r])
            res = max(curr,res)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return res
        