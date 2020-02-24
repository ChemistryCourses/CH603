import numpy as np
def read_2_e(nbasis):

 
#define the 4 d array
 twoe=np.zeros([nbasis,nbasis,nbasis,nbasis])

 return twoe
#####################################################################
nbasis=7   
f= open("eri.out","w")     
twoe=read_2_e(nbasis)
for i in range(nbasis):
   for j in range(nbasis):
     for k in range(nbasis):
       for l in range(nbasis):
                print(i+1,j+1,k+1,l+1,"{:.7f}".format(twoe[i,j,k,l]))
                f.write(str(i+1)+' '+str(j+1)+' '+str(k+1)+' '+str(l+1)+' '+str(twoe[i,j,k,l])+'\n')
f.close() 
