"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
   
    
    if(head.next == None):
        return(head)
    
    else:
        current = head
        prev = None
        #Traversing to the end
        while(current.next != None):
            
            following = current.next
            current.next = prev
            prev = current
            current = following
            
        current.next = prev    
        head = current
        
        return(head)
