def has_cycle(head):
    
    if(head == None or head.next == None):
        return(False)
    
    current = head
    that_list = []
    while(current.next != None):
        
        that_list.append(current)
        
        current = current.next
        
        if(current.next in that_list):
            return(True)
        else:
            continue