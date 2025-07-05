# Problem: 169 – majority Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/majority-element/description/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore majority vote
        count = candidate = 0
        for x in nums:
            if count==0:
                candidate = x
                count+=1
            elif x== candidate:
                count+=1
            else:
                count-=1
    
        return candidate
        