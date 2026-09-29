# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            after = curr.next # get next node
            curr.next = prev  # set curr node to previous one
            prev = curr       # set new previous to current node
            curr = after      # iterate node

        return prev
