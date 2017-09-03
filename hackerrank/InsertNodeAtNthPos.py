"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if(head==None):
        head = Node(data,None)
    
    elif(head.data):
        
        if(position==0):
            newNode=Node(data,head)
            head=newNode
            
        else:
            current = head
            counter=0
            while(counter<position):
                prev = current
                current = current.next
                ToReplace = current
                counter+=1
                
            newNode = Node(data, ToReplace)     
            prev.next = newNode
        
            
    return(head)        
