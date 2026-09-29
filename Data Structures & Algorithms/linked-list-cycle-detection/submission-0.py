# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = 0, 0
        fp, sp = head, head

        while True:
            for i in range(0, 2):
                if fp.next != None:
                    print(f"fp advancing to {fp.val}")
                    fp = fp.next
                else:
                    return False
            
            if sp.next != None:
                sp = sp.next
            else:
                return True

            if fp == sp:
                return True