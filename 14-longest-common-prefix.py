# Problem: 14 – Longest Common Prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            j = 0
            while j < len(prefix) and j < len(s) and prefix[j] == s[j]:
                j += 1
            prefix = prefix[:j]
            if not prefix:
                return ""
        return prefix
        