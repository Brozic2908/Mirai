# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        tail = ListNode
        prev_tail = ListNode
        
        while head.next != null:
            prev_tail.val = head.val
            tail.next = prev_tail
            prev_tail = tail
            head = head.next

        return prev_tail