# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNodes(head: ListNode):
    current = head
    prev = None
    
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
    
    newNode = ListNode()
    newHead = newNode
    maxNum = prev.val
    while prev:
        if maxNum == prev.val:
            newHead.next = ListNode(maxNum)
            newHead = newHead.next
        
        if maxNum < prev.val:
            maxNum = prev.val
            newHead.next = ListNode(maxNum)
            newHead = newHead.next
        prev = prev.next

    current2 = newNode.next
    prev2 = None
    
    while current2:
        next2 = current2.next
        current2.next = prev2
        prev2 = current2
        current2 = next2
    return prev2
    
def printNode(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

    
head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
head = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1)))))

printNode(head)


printNode(removeNodes(head))
