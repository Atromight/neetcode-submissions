# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        n = 0
        while tail is not None:
            n += 1
            tail = tail.next

        div = n // k
        mod = n % k

        curr = head
        curr_tail = None
        for i in range(div):
            prev = None
            j = 0
            while j < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                if j == 0:
                    curr_tail = prev

                j += 1

            if i == 0:
                res = prev
                conn_head = curr_tail

            else:
                conn_tail = prev
                conn_head.next = conn_tail
                conn_head = curr_tail

        if mod:
            conn_head.next = curr
        
        return res



        