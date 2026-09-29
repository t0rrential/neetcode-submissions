# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode

        if list1 and list2:
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        else:
            if list1 == None:
                return list2
            if list2 == None:
                return list1
            

        # i hate if statements

        headhead = head
        while head:
            if list1 != None and list2 != None:
                l1, l2 = list1.val, list2.val

                if l1 > l2:
                    head.next = list2
                    head = head.next
                    list2 = list2.next
                
                else:
                    head.next = list1
                    head = head.next
                    list1 = list1.next
            
            elif list1 == None:
                head.next = list2
                head = head.next
                break
            elif list2 == None:
                head.next = list1
                head = head.next
                break

        return headhead
