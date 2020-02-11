import numpy as np 

def file_read(file_name,nbasis):

 #open the file

 #read the file using readline to file_content

 #close the file
 A=np.zeros([nbasis,nbasis])

 for line in file_content:
    V_line=line.rstrip
    V_line=V_line.split() 
 return A
