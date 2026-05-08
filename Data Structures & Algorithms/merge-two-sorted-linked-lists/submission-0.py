# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None

        if list1.val < list2.val:
            val = list1.val
            list1 = list1.next

        else:
            val = list2.val
            list2 = list2.next

        return ListNode(val, self.mergeTwoLists(list1, list2))
