# Problem: 76 – minimum window substring
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-window-substring/description/

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        required = len(need)
        have = 0
        ans = float("inf"),0,0
        l = 0
        
        for r,ch in enumerate(s):
            window[ch]+=1
            if window[ch]==need[ch]:
                have+=1
            
            while l<=r and have==required:
                if r-l+1 < ans[0]:
                    ans = r-l+1,l,r
                
                fir_wind_ch = s[l]
                window[fir_wind_ch]-=1
                if window[fir_wind_ch] < need[fir_wind_ch]:
                    have-=1
                l+=1
        length, l, r = ans
        return "" if length==float("inf") else s[l:r+1]