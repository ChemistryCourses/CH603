password='12345'
failure=0
while password!='xyz':
 print('wrong password')
 failure=failure+1
 continue
 if failure >3:
   break
 
