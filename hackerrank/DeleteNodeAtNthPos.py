"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if(head==None):
        return
    
    elif(head.data):
        
        if(position==0):
            newHead = head.next
            head = None
            head = newHead
            return(head)
            
        else:
            current = head
            counter = 0
            while(counter<position):
                prev = current
                current = current.next
                ToDelete = current
                nextNode = ToDelete.next
                
                counter+=1
            
            ToDelete = None
            prev.next = nextNode          
        
            
    return(head)     
