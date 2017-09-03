'''
a = []
N_M = [int(k) for k in input().split(" ")]





for i in range(N_M[0]):
    a.append(0)

Ops = []
for i in range(N_M[1]):
    Ops.append([int(k) for k in input().split()] )
    #Taking care Ops[i][2] and Ops[i][1] limit.
   

for i in range(N_M[1]):
    if(Ops[i][0]==Ops[i][1]):
        a[ Ops[i][0]-1  ]+= Ops[i][2]
        
    else:
        for k in range(Ops[i][ 0 ]-1, Ops[i][ 1 ]):
            a[k] += Ops[i][2]
        
print(max(a))
'''

a = []
N_M = [int(k) for k in input().split(" ")]

'''
#Taking care of N and M limits.
if(N_M[0]<3):
    N_M[0]=3    
elif(N_M[0]>10**7):
    N_M[0] = 10**7
if(N_M[1]<1):
    N_M[0]=1
elif(N_M[1]>(2*(10**5))):
    N_M[1] = 2*(10**5)
'''

#This uses prefix sum algo to minimize complexity.
    
for i in range(N_M[0]):
    a.append(0)

Ops =[]

for i in range(N_M[1]):
    Ops.append([int(k) for k in input().split()] )
    
    a[Ops[i][0]-1]+=Ops[i][2]
    if(len(a)==Ops[i][1]):
        continue
        
    a[Ops[i][1]]-=Ops[i][2]

#Applying the pre fix sum thing, and calculating accumulated sum at each index.

for i in range(1,len(a)):
    a[i]+=a[i-1]
        
        
print(max(a))
