# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1, v2 = 0, 0
        carry = 0
        dummy = ListNode()
        add = dummy

        while l1 or l2 or carry:
            v1, v2 = 0, 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            v = v1 + v2
            print(v)
            if carry:
                v += 1
                carry = 0
            if v >= 10:
                carry += 1
                v -= 10

            add.val = v
            print(v)
            if l1 or l2 or carry:
                n = ListNode()
                add.next = n
                add = n

        return dummy
            