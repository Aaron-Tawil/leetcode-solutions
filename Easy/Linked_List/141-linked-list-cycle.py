# Problem: 141 – linked list cycle
# Difficulty: Easy
# Link: https://leetcode.com/problems/linked-list-cycle/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p = fast_p = head
        if not head: return False
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if fast_p is slow_p: return True

        return False 

        