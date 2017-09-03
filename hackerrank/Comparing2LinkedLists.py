"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    
    if(headA == None or headB == None):
        if(headA == headB):
            return(1)
        else:
            return(0)
    
    elif(headA.next == None or headB.next == None):
        if(headA.next==headB.next):
            if(headA.data == headB.data):
                return(1)
            else:
                return(0)
        else:
            return(0)
        
    else:
        current1=headA
        current2=headB
        while(current1.next!=None and current2.next!=None):
            if(current1.data != current2.data):
                return(0)
            current1 = current1.next
            current2 = current2.next
        
        if(current1.next != current2.next):
            return(0)
        else:
            return(1)
