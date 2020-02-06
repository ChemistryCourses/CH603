import numpy as np
import math

## reading hessian.txt
hess_file=open('hessian.txt')
hess_content=hess_file.readlines()
hess_file.close()

## storing hessian in a numpy array
temp_hess=[]
for line in hess_content:
  v_line=line.rstrip()
  f=v_line.split()
  temp_hess.append(f)

#calculate the no of atoms
num_atoms=int(temp_hess[0][0])

#convert the hessian from a rectangular to square matrix
hessian=np.zeros([3*num_atoms,3*num_atoms])
k1=0
k2=0
for i in range(3*num_atoms*num_atoms):
  for j in range(3):
    hessian[k1][k2]=temp_hess[i+1][j]
    k1=k1+1
    if(k1>=3*num_atoms):
      k1=0
      k2=k2+1
