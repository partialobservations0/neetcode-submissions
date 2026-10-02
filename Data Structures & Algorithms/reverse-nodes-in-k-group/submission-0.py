# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def get_n_nodes(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        def reverse_linked_list(head,k):
            prev = None
            curr = head

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            head.next = curr
            return prev
        
        n = get_n_nodes(head)
        groups = n // k
        
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy
        curr = head

        for _ in range(groups):
            group_start = curr
            new_head = reverse_linked_list(curr,k)
            group_prev.next = new_head
            group_prev = group_start
            curr = group_start.next

        return dummy.next



        