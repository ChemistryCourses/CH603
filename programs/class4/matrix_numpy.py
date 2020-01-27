import numpy as np
import time
# intilize A and B
A=np.zeros([500,500])
B=np.zeros([500,500])
for i in range(len(A)):
   for j in range(len(A[0])):  
      A[i][j]=i/(j+1)
for i in range(len(B)):
   for j in range(len(B[0])):  
      B[i][j]=j/(i+1)
print ('matrix multiplication started')
tic=time.time()
 
C=np.matmul(A,B)
toc=time.time()
print('multiplication done')
print('time required '+str(toc-tic)+' sec')
