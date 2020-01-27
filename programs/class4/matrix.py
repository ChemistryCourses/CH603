#This is a program to write matrix multiplication

#Take a 3*3
A=[[12,7,3],
  [4,5,6],
  [7,8,9]]

#Take a 3*4 Matrix
B=[[5,8,1,2],
   [6,7,3,0],
   [4,5,9,1]]
C=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]
print (len(B[0]))
for i in range(len(A)):
   for j in range (len(B[1])):
      for k in range(len(B)):
         C[i][j]+=A[i][k]*B[k][j]
print ('product matrix ')
print (C)
