# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        new_h = None
        temp = None
        if p2.val >= p1.val:
            new_h = p1
            next_temp = p1.next
            p1.next = p2
            p1 = next_temp
        else:
            new_h = p2
            next_temp = p2.next
            p2.next = p1
            p2 = next_temp

        while p1 != None or p2 != None:
            if p2.val >= p1.val:
                new_h = p1
                next_temp = p1.next
                p1.next = p2
                p1 = next_temp
            else:
                new_h = p2
                next_temp = p2.next
                p2.next = p1
                p2 = next_temp

        return new_h



