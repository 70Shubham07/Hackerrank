current = head
    length = 0
    
    '''
    if( head.next == None ):
        return(head.data)
    
    elif(head == None):
        return(0)
    '''
    
    while( current.next != None ):
        current = current.next
        length+=1
    
    length+=1
    
    pos = length - position - 1
    posS = 0
    current = head
    
    while( posS != pos ):
        current = current.next
        posS+=1
    
    return(current.data)
    