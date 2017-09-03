def SortedInsert(head, data):
    if(head == None):
        head=Node()
        head.data = data
        head.prev = None
        head.next = None
        return(head)
    
    the_new  = Node()
    the_new.data = data
    the_new.prev=None
    the_new.next=None
    
    current = head
    previous = None
    #if(current==head):
    #    print("true")
    
    while( current.next != None ):   # this current.next thing is causing a lot of problems.
    
        if( data <= current.data ):
    
            the_new.next = current
            the_new.prev = previous
    
            if( previous == None ):
                return(the_new)
    
            else:
                previous.next = the_new
                return(head)
        ''' 
        if(current.next == None):
            the_new.prev = current
            current.next = the_new
            the_new.next = None
            break
            
        '''    
            
    
        previous = current      #previous will ultimately hold the penultimate node
        current = current.next  #the final value of current will be the ultimate node
    
    
    #previous = current
    #return(head)    
    
    #'''
    if( current == head ):                      #There must be some problem with this!
    
        if(data <= head.data):
    
            the_new.prev = None
            the_new.next = head
            head.prev = the_new
            return(the_new)
        
        else:
            
            head.next = the_new
            the_new.prev = head
            the_new.next = None
            return(head)
                


    elif(current.next == None):
        
        if(data<=current.data):
            the_new.next = current
            the_new.prev = previous
            
            previous.next = the_new
            current.prev = the_new
            return(head)
            
        else:
            
            the_new.next = None
            current.next = the_new
            the_new.prev = current
            return(head)
        
    
    
            




            


            
            
        
        
         

            

            

            
