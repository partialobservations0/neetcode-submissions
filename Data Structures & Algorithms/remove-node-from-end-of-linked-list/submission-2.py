# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # main point is to remove the node which require
        # setting the previous node's next to nth node's next

        # first to find the nth node
        # then replace the node

        # since it is nth Node from end, we can find the length of the list
        # and then find the node we need to move

        def findLength(head):
            i = 0
            if not head:
                return i
            while head:
                i += 1
                head = head.next
            return i

        length_of_list = findLength(head)
        if length_of_list == 1 and n == 1:
            return None

        n_from_start = length_of_list - n 
        if n_from_start == 0:
            return head.next
        curr = head
        while n_from_start - 1 > 0:
            curr = curr.next
            n_from_start -= 1
        
        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None

        return head

