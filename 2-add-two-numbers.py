# Problem: 2 – add two numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/add-two-numbers/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = last = ListNode()
        t, val = divmod(l1.val + l2.val,10) 
        head.val = val
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            t,val = divmod(l1.val + l2.val+t,10)
            new = ListNode(val)
            last.next = new
            last = last.next
            l1 = l1.next
            l2 = l2.next
        
        l = l1 if l1 else l2
        while l:
            t,val = divmod(l.val + t,10)
            new = ListNode(val)
            last.next = new
            last = last.next
            l = l.next
        if t:
            new = ListNode(t)
            last.next = new
            last = last.next
        return head