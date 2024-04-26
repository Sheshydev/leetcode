from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()

        print("--------")
        self.printList(list1)
        self.printList(list2)
        self.printList(list3)

        while list1 and list2:
            if list1.val <= list2.val:
                list1 = self.transferHeadToEnd(list1, list3)
            else:
                list2 = self.transferHeadToEnd(list2, list3)
            print("--------")
            self.printList(list1)
            self.printList(list2)
            self.printList(list3)
        
        if list1 is not None:
            list3_tail = self.getTail(list3)
            list3_tail.next = self.list1

        if list2 is not None:
            list3_tail = self.getTail(list3)
            list3_tail.next = list2

        print("--------")
        self.printList(list1)
        self.printList(list2)
        self.printList(list3)

        return list3.next


    def transferHeadToEnd(self, src: ListNode, dest: ListNode):
        dest_tail = self.getTail(dest)
        dest_tail.next = src
        if src is not None:
            src = src.next
        
        dest_tail = dest_tail.next
        dest_tail.next = None

        return src

    def getTail(self, node: ListNode):
        while node.next is not None:
            node = node.next
        
        return node
    

    def printList(self, node:ListNode):
        while node is not None:
            print(str(node.val) + "-", end='')
            node = node.next
        print(end='\n')

l1 = ListNode(1,ListNode(2,ListNode(4,None)))
l2 = ListNode(1,ListNode(3,ListNode(4,None)))

sol = Solution()

res = sol.mergeTwoLists(l1, l2)