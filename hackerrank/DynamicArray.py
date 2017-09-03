#Taking the input first!


N_Q = [int(n_q) for n_q in input().strip().split(' ')  ]
lastAnswer = 0
Q = []
seqList = []
for i in range(N_Q[0]):
    b=[]
    seqList.append(b)

for i in range(N_Q[1]):
    Q.append([int(c) for c in input().strip().split()])
   
#Next, I iterate through the queries.

for i in Q:
    
    if( i[0] ==  1):
        idx = (i[1]^lastAnswer)%N_Q[0]
        seqList[idx].append(i[2])
        
    elif(i[0] == 2):
        idx0 = (i[1]^lastAnswer)%N_Q[0]
        idx1 = i[2]%len(seqList[idx0])
        lastAnswer = seqList[idx0][idx1]
        print("{0}".format(lastAnswer))