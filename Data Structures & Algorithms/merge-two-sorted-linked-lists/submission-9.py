# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummy_node = ListNode(-1)
        tail = dummy_node

        while p1 != None or p2 != None:
            if p2.val >= p1.val:
                temp = ListNode(p1.val)
                tail.next = temp
                tail = temp
                p1 = p1.next
            else:
                temp = ListNode(p2.val)
                tail.next = temp
                tail = temp
                p2 = p2.next
            if p1 == None:
                tail.next = p2
            else:
                tail.next = p1

        return dummy_node.next



