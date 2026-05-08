# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = ""
        number2 = ""
        while l1 is not None:
            number1 = str(l1.val) + number1
            l1 = l1.next
        
        while l2 is not None:
            number2 = str(l2.val) + number2
            l2 = l2.next
        
        number3 = str(int(number1) + int(number2))

        l3 = None
        for i in range(len(number3)):
            num = int(number3[i])
            l3 = ListNode(num, l3)
        
        return l3
        

        