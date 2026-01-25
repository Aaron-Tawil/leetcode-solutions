# Problem: 394 – decode string
# Difficulty: Medium
# Link: https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the full number (handles multi-digit numbers like '100')
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # We are entering a new nested level.
                # Push the string we've built so far and the multiplier to the stack.
                stack.append((curr_str, curr_num))
                # Reset for the new level
                curr_str = ""
                curr_num = 0
            elif char == ']':
                # We finished a level. Pop the previous context.
                prev_str, num = stack.pop()
                # Repeat the current string and attach it to the previous string.
                curr_str = prev_str + (num * curr_str)
            else:
                # It's a regular letter, just add it to our current string.
                curr_str += char
                
        return curr_str
        
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




        