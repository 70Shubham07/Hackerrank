"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    
    if(headA==None and headB==None):
        return(None)
    
    elif( headA==None and headB):
         return(headB)
    elif(headB==None and headA):
        return(headA)
    elif(headA.next==None or headB.next==None):
        if(headA.next==headB.next):
            if(headB.data>headA.data):
                headA.next = headB
                return(headA)
            else:
                headB.next = headA
                return(headB)
            
        elif(headA.next==None and headB.next):
            if(headA.data<headB.data):
                headA.next = headB
                return(headA)
            
            elif(headA.data>headB.data):
                current=headB
                while(current.data<headA.data):
                    prev=current
                    current=current.next
                
                prev.next=headA
                headA.next = current
                return(headB)
            
        elif(headA.next and headB.next==None):
            if(headB.data<headA.data):
                headB.next = headA
                return(headB)
                
            elif(headB.data>headA.data):
                current=headA
                while(current.data < headB.data):
                    prev=current
                    current=current.next
                
                prev.next=headB
                headB.next = current
                return(headA)
            
        
    else:
        ref = headA
        sec = headB
        current1=ref
        current2=sec
        
        prev = None
        while(current2.next!=None):
            while( (current1.next!=None) and (current2.data>current1.data)):
                #insert current2.data between the data before current1.data and it
                prev = current1
                current1 = current1.next
                
            if(current2.data<=current1.data):
                nextInSec = current2.next
                current2.next = current1
                if(prev!=None):
                    prev.next = current2
                elif(prev==None):
                    headA = current2
                    
                prev = current2
                #current1 = current1.next
                current2 = nextInSec
                
            elif(current1.next==None):
                current1.next = current2
                #current2 = current2.next 
                return(headA)
        #Deciding position of last element of secondary list    
        #What will be the last element? prev? No. It'll be current1
        while(current1.next!=None):
            if(current2.data < current1.data):
                prev.next = current2
                current2.next = current1
                
                
                return(headA)
        
            current1 = current1.next
            
        if(current1.next==None):
            current1.next = current2        
            
                
                
                
        return(headA)    
