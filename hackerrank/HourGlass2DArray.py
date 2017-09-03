#Hourglass - 2D arrays.

#!/bin/python3

import sys


arr = []
#Taking input for the array.
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
final_list = []
iter = 0
diction = {}
for row in range(4):
    for col in range(4):
        diction[iter] = [row,col]
        a1=arr[row][col:col+3]
        a2=arr[row+1][col+1]
        a3=arr[row+2][col:col+3]
        s = sum(a1)+a2+sum(a3)
        final_list.append(s)   
        iter+=1
        
answer = max(final_list)
row_col = diction[ final_list.index(answer) ]

print(answer)
# I have to complete one row, before moving to next. In 2nd row, I have to leave spaces.
# Outer loop for rows. Inner loop for columns, with 2 conditional statements.
'''
for row in range(row_col[0], row_col[0]+3):
    for col in range(row_col[1], row_col[1]+3):
        if(row == row_col[0]+1):
            print("\n  {0}  ".format(arr[row][col]))
            break
        else:
            print(arr[row][col], end = " ")
'''    
