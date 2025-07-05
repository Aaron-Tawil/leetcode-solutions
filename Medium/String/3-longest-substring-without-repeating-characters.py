# Problem: 3 – longest substring without repeating chars
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mx = 0 
        seen = {}
        for r, ch in enumerate(s):
            if ch in seen and seen[ch] >= l:
                l = seen[ch]+1
            seen[ch] = r
            mx = max(mx,r-l+1) 
        return mx

        