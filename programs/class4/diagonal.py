import numpy as np
A=np.array([[12,7,3],
  [4,5,6],
  [7,8,9]])
w,v=np.linalg.eig(A)
print('eigen values')
print(w)
print('eigen vectors')
print(v)


