# Problem: 394 – decode string
# Difficulty: Medium
# Link: https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        idx = 0
        def parse():
            nonlocal idx
            if idx>=n:
                return ""
            elif s[idx]==']': #finish this seq
                idx+=1
                return ""
            elif s[idx].isdigit():
                #scan the integer and move on to parse inside bracket
                start = idx
                while s[idx]!='[':
                    idx+=1
                k = int(s[start:idx])
                idx+=1 #skip the '['
                decode = k * parse()
                return decode + parse()
            else: # it is a letter
                c = s[idx]; idx+=1
                return c + parse()
        
        return parse()




        