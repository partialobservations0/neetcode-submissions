# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverse_list(head):

            if not head: 
                return None
            curr = head
            prev = None
            l = 1
            while curr:

                nextn = curr.next
                curr.next = prev
                
                prev = curr
                curr = nextn
                l+=1
            
            return prev,l


        def combine_list(h, r,l):
            mylist = []
            for i in range(0,l):
                if i % 2 == 0:
                    mylist.append(h)
                    h = h.next
                else:
                    mylist.append(r)
                    r = r.next
                print(i)

            for i in range(0,l):
                mylistl[i].next = mylistl[i+1]
            
            return l[0]
        
        ithead = head
        mylist = []
        while ithead:
            mylist.append(ithead)
            ithead = ithead.next
        
        i = 0
        j = len(mylist) - 1
        while i < j:
            mylist[i].next = mylist[j]
            i += 1
            if i >= j:
                break
            mylist[j].next = mylist[i]
            j -= 1
        mylist[i].next = None


        #head = mysol[0]        
        
        #return mysol[0]
        #rhead,l = reverse_list(headc)
        #return combine_list(head,rhead,l)


        

