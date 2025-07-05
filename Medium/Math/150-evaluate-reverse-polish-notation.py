# Problem: 150 – evaluate reverse polish notation
# Difficulty: Medium
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for tok in tokens:
            if tok not in "+-*/":
                st.append(int(tok))
            else:
                b, a = st.pop(), st.pop()
                if tok == '+': st.append(a + b)
                elif tok == '-': st.append(a - b)
                elif tok == '*': st.append(a * b)
                elif tok == '/': st.append(int(a / b))
        return st[0]
        