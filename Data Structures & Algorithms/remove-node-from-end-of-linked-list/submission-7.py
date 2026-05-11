# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        lead=head
        cur=head
        for i in range(n):
            lead=lead.next
        if lead is None:
            return head.next
        while lead.next is not None:
            cur=cur.next
            lead=lead.next
        cur.next=cur.next.next
        return head