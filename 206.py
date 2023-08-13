class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        p1 = None
        p2 = head
        p3 = head.next

        while p2 is not None:
            p2.next = p1
            p1 = p2
            p2 = p3
            if p3 is not None:
                p3 = p3.next
            
        return p2
