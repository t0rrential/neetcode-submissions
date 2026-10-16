# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []

        for n in lists:
            if n:
                l.append(n.val)
                while n.next:
                    n = n.next
                    l.append(n.val)

        l.sort()

        if l:
            f = ListNode(val=l.pop(0), next=None)
            fo = f
            for v in l:
                c = ListNode(val=v, next=None)
                f.next = c
                f = c

            return fo


        