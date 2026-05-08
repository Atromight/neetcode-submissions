# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = None
        tail = head
        for l in lists:
            while l is not None:
                val = l.val
                if head is None:
                    head = ListNode(val)
                    tail = head

                elif val <= head.val:
                    head = ListNode(val, head)
                
                elif val >= tail.val:
                    tail.next = ListNode(val)
                    tail = tail.next

                else: # val > head.val and val < tail.val
                    curr = head
                    while curr.next and curr.next.val < val:
                        curr = curr.next

                    curr.next = ListNode(val, curr.next)

                l = l.next

        if head is None:
            return None
        else:
            return head


