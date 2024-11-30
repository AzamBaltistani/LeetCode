class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1, l2):
    sumList = ListNode()
    sumList_tail  = sumList
    
    carry = 0
    while l1 or l2 or carry:
        d1 = l1.val if l1 else 0
        d2 = l2.val if l2 else 0
        s = d1 + d2 + carry
        carry = s//10
        s %=10
        sumList_tail.next = ListNode(s)
        sumList_tail = sumList_tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return sumList.next

def printNode(l = ListNode(0)):
    temp = l
    while temp is not None:
        print(temp.val, end=' ')
        temp = temp.next
    print()
ll1 = [2,4,3]
l1 = ListNode()
l1_tail  = l1

for i in range(len(ll1)-1):
    l1_tail.val = ll1[i]
    l1_tail.next = ListNode(ll1[i+1])
    l1_tail = l1_tail.next
    
printNode(l1)
ll2 = [5,6,4]
l2 = ListNode()
l2_tail  = l2
for i in range(len(ll2)-1):
    l2_tail.val = ll2[i]
    l2_tail.next = ListNode(ll2[i+1])
    l2_tail = l2_tail.next
    
printNode(l2)

printNode(addTwoNumbers(l1,l2))
# [7,0,8]