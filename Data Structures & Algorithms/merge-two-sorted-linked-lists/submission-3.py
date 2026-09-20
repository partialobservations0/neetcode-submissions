# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def exchange_vars(result, listnum):
            result.next = ListNode(listnum.val) 
            return result.next, listnum.next
            
        
        if not list1: 
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            result = list1
            result_copy = list1
            list1 = list1.next
        else:
            result = list2
            result_copy = list2
            list2 = list2.next

        while list1 and list2: 
            if list1.val <= list2.val:
                result, list1 = exchange_vars(result, list1)
            else:
                result, list2 = exchange_vars(result, list2)

        if list1:
            while list1:
                result, list1 = exchange_vars(result, list1)
        if list2:
            while list2:
                result, list2 = exchange_vars(result, list2)

        return result_copy           
            