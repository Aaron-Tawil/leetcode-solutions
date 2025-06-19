# Problem: 5 – longest palindromic substring
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
       
        best = ""
        for mid in range(len(s)):
            lo,ro = mid-1,mid+1
            while 0<=lo and ro<len(s) and s[lo]==s[ro]:
                lo-=1
                ro+=1
            pal_odd = s[lo+1:ro]
            if len(pal_odd) > len(best):
                best = pal_odd

            le, re = mid-1,mid
            while 0<=le and re<len(s) and s[le]==s[re]:
                le-=1
                re+=1
            pal_ev = s[le+1:re]
            if len(pal_ev) > len(best):
                best = pal_ev
        
        return best