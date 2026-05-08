# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        if not head:
            return head

        while head.val is not None:
            vals.append(head.val)
            if head.next:
                head = head.next
            else:
                break

        node = ListNode(vals.pop(0))
        while vals:
            val = vals.pop(0)
            node = ListNode(val, node)

        return node


        