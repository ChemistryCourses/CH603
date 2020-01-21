#This is a program to write matrix multiplication
import time

#Take a 1000*1000
A=[]
for i in range(10000):
   D=[]
   for j in range(1000):
      D.append(float(i)/float(j+1))
   A.append(D)


#Take a 1000*1000 Matrix
B=[]
for i in range(1000):
   D=[]
   for j in range(1000):
      D.append(float(j)/float(i+1))
   B.append(D)

#initialize C
C=[]
for i in range(len(A)):
   D=[]
   for j in range(len(B[0])):
      D.append(0)
   C.append(D)
