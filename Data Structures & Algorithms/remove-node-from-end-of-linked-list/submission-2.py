# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = right = dummy

        # Tạo cửa số trượt với độ dài n. Tức là Right của cửa số chạm null thì left cũng đã đứng ngay vị trí node cần xóa
        for _ in range(n):
            right = right.next

        while right.next:
            right = right.next
            left = left.next
        
        left.next.next = right
        return dummy.next