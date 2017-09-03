"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    current = head
    rev = []
    if(head==None):
        return
    
    while(current.next!=None):
        rev.append(current.data)
        current = current.next
    
    rev.append(current.data)
    if(len(rev)==1):
        print(rev[0])
        
    rev.reverse()
    for i in range( len(rev) ):
        print(rev[i])
        
