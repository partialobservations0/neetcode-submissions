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
        
        def copy_list_to_result(result, listnum):
            while listnum:
                result, listnum = exchange_vars(result, listnum)
            return result

        def init_result(listnum):
            result = listnum
            result_copy = listnum
            listnum = listnum.next
            return result, result_copy, listnum
        
        if not list1: 
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            result, result_copy, list1 = init_result(list1)
        else:
            result, result_copy, list2 = init_result(list2)

        while list1 and list2: 
            if list1.val <= list2.val:
                result, list1 = exchange_vars(result, list1)
            else:
                result, list2 = exchange_vars(result, list2)

        if list1:
            result = copy_list_to_result(result,list1)
        if list2:
            result = copy_list_to_result(result,list2)

        return result_copy           
            