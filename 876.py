# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        
        count = 0
        p = head
        while p:
            count += 1
            p = p.next

        mid_idx = count//2 + 1
        p = head
        for i in range(mid_idx - 1):
            p = p.next
        return p
    
sol = Solution()
res = sol.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
print(res.val)