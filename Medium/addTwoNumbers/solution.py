# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = ListNode()
        b = a
        c = 0
        while l1 or l2 or c:
            if l1:
                d = l1.val
            else:
                d = 0
            if l2:
                e = l2.val
            else:
                e = 0
            f = d + e + c
            c = f // 10
            f %= 10
            b.next = ListNode(f)
            b = b.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        return a.next