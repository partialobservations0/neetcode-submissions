"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # lets say there is only one node 
        # how do i copy it

        # so we need the node value, next node and even random node 
        # to copy
        # now we can create a list of nodes that copy all nodes
        # in the given linkedlist and then make connections later
        
        # now we have a list of nodes 
        # from the existing linked list we can copy the index of node the 
        # random prop points to and then use our list to point to that node

        if not head:
            return None
        randommap = {}
        allnodes = []
        iteratorhead = head
        while iteratorhead:
            randommap[iteratorhead] = Node(iteratorhead.val)
            iteratorhead = iteratorhead.next

        iteratorhead = head
        chead = randommap[head]
        while head:
            chead.next = randommap[head.next] if head.next else None
            chead.random = randommap[head.random] if head.random else None
            if chead:
                print(chead.val)

            head = head.next
            chead = chead.next

        return randommap[iteratorhead]
        
