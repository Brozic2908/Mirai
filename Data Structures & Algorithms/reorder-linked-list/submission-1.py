
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None or head.next.next == None:
            return None
        h = head
        temp1 = h.next

        last_node, prev_last_node = self._lastNode(h)

        if last_node == None or prev_last_node == None:
            return None  

        h.next = last_node
        last_node.next = temp1
        prev_last_node.next = None

        print(f"NextNode: {temp1.val}")
        print(f"lastNode: {last_node.val}")
        self.reorderList(temp1)

    def _lastNode(self, node: Optional[ListNode]) -> None:
        if node == None or node.next == None:
            return None, None
        while (node.next != None):
            prev = node
            node = node.next
        
        return node, prev
    