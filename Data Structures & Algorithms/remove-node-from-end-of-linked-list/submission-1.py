# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        counter_head = head
        while counter_head:
            cnt += 1
            counter_head = counter_head.next

        i = 0
        curr = head
        if cnt == 1:
            return None

        elif cnt == n:
            head = head.next
            return head

        while i < cnt - n:
            print(head.val, curr.val)
            i += 1
            if i == cnt - n:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head

