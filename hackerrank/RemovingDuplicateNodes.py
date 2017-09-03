def RemoveDuplicates(head):
    
    if(head==None or head.next==None):
        return(head)
    
    current = head
    while(current.next != None):
        
        prev = current
        current = current.next
        
        if(prev.data == current.data):
            prev.next = current.next
            current = prev
         
    
    return(head)