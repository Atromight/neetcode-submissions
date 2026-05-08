# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        head.val = "visited"
        while head.next is not None:
            head = head.next
            if head.val == "visited":
                return True

            head.val = "visited"

        return False
