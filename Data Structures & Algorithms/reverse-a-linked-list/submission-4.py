# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            return self.addNode(head, None)

    def addNode(self, head: Optional[ListNode], node: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(head.val, node)
        if head.next is None:
            return node
        else: # head.next is not None
            head = head.next
            return self.addNode(head, node)

        
