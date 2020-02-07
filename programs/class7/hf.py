#This a program to calculate the Hatree-Fock energy of a closed shell molecule
#Read the geometry
input_file=open('geom.dat')   #open the file

file_content=input_file.readlines()# read the content

input_file.close()            # close the file

#print(file_content)


# store the input in list
temp_geom=[]
for line in file_content:
  v_line=line.rstrip()
  if len(v_line)>0:
   temp_geom.append(v_line.split())

print(temp_geom)


#no of atoms
NATOM=int(temp_geom[0][0])
print('Total no of atom '+str(NATOM))
ATOM_SYMBOL=[] # this list contains the atom symbols
for i in range(1,NATOM+1): 
 ATOM_SYMBOL.append(temp_geom[i][0])
print(ATOM_SYMBOL)
