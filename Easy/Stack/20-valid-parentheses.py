# Problem: 20 – Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch in ['[','{','(']:
                st.append(ch)
            else:
                if len(st) ==0 :
                    return False
                open = st.pop()
                if (open == '[' and ch!=']') or (open == '{' and ch!='}') or (open == '(' and ch!=')'):
                    return False       
        return not st
