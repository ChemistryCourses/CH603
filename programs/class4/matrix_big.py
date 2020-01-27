import time

#Take a 500*500
A=[]
for i in range(500):
   D=[]
   for j in range(500):
      D.append(float(i)/float(j+1))
   A.append(D)


#Take a 500*500 Matrix
B=[]
for i in range(500):
   D=[]
   for j in range(500):
      D.append(float(j)/float(i+1))
   B.append(D)

#initialize C
C=[]
for i in range(len(A)):
   D=[]
   for j in range(len(B[0])):
      D.append(0)
   C.append(D)
print('multiplication starts')
tic=time.time()
for i in range(len(A)):
   for j in range (len(B[1])):
      for k in range(len(B)):
         C[i][j]+=A[i][k]*B[k][j]
toc=time.time()
print ('multiplication done ')
print('time taken '+str(toc-tic)+ 'secs')
