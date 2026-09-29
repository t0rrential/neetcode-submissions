# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head

        while f and f.next:
            f = f.next.next
            s = s.next

        curr = s.next
        prev = s.next = None

        while curr:
            after = curr.next # get next node
            curr.next = prev  # set curr node to previous one
            prev = curr       # set new previous to current node
            curr = after      # iterate node

        l1 = head # 2
        l2 = prev # 8

        while l2:
            l1n, l2n = l1.next, l2.next

            l1.next = l2
            l2.next = l1n

            l1, l2 = l1n, l2n
