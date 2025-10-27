# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        pointers = []
        while curr:
            pointers.append(curr)
            curr = curr.next
        
        curr = head
        times = len(pointers)//2
        for i in range(times):
            temp = curr.next
            curr.next  = pointers[-1-i] #check if it is correct
            curr.next.next = temp
            curr = temp
        curr.next = None

    # O(1) memory
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1) middle (slow/fast)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) reverse second half
        prev, cur = None, slow.next
        slow.next = None  # split
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        l1, l2 = head, prev

        # 3) merge (weave)
        while l2:
            n1, n2 = l1.next, l2.next
            l1.next = l2
            l2.next = n1
            l1, l2 = n1, n2