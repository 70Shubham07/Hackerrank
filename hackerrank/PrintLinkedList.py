"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
"""
'''
 class Node:
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
class LinkedList:
    def __init__(self, head, length):
        self.head = head
        self.length = length
'''
        
        
def print_list(head):
    
    
    current = head
    if( current.next == None and current.data ):
        print(self.current.data)
        return
    
    elif(current.next == None and current.data == None):
        return
        
    while(current.next != None):
        print(current.data)
        current = current.next
    
    print(current.data)
    return
