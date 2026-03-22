class Solution:
    def trap(self, height: List[int]) -> int:
        #2pointers
        n = len(height)
        lm = height[0]
        rm = height[n-1]
        l = 0
        r = n-1
        res = 0
        while l<r:
            if lm<=rm:
                res += lm-height[l]
                l+=1
                lm = max(lm,height[l])
            else:
                res += rm-height[r]
                r-=1
                rm = max(rm,height[r])
        return res

        #dp
        n = len(height)
        l_m = [0] * n 
        r_m = [0] * n
        l_m[0] = height[0]
        r_m[n-1] = height[n-1]

        for i in range(1,n):
            l_m[i] = max(height[i], l_m[i-1])
        
        for i in range(n-2,-1,-1):
            r_m[i] = max(height[i], r_m[i+1])

        res = 0
        for i in range(n):
            res +=  min(l_m[i],r_m[i]) - height[i]
        return res

        