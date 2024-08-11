from __future__ import print_function
import sys
import os
import string
import __future__

from time import time

sys.stdout.write(str(time())+"\n")
print(sys.path)
print ('I AM PROGRAMER DESIGN \n Yes')

count = 0
put=[]

#common factor
factor = 0
nt = 0

for a in range(10):   
    count = count+1
    print(a," Num (",count,")->time")	   
    if a == 9:
     print("\n")
  
#p,k = map(int,input("Please input 2 common factor here ,TKS!").split())	#for python3.X
#p,k = map(int, raw_input("Please input 2  number here ,TKS!---> ").split())  
p,k = input("Enter a two value: ").split() 
array = (a+1)*(a+1)
weigth = array /2
#mux = p**k
mux = int(p)*int(k)
combe = 0;
check = 0


#print('total array size = ',array ,'array size half is = ',weigth )

# for t in range (array):
for t in range (array+1):
    if (t%mux) == 0:
     put.append(t)

listput =len(put)	
sel = 0

print(put, 'len = ',listput)	  
print('')
	
for num in range (a+2):
    for num2 in range(a+2):	
     check =0
     combe = combe + 1	    
    if num2 == (a+1):
     print('|') 
    else:
     for sel in range (listput):
      if combe == put[sel]:
       nt = nt + 1
       print('O',end='')			 
    #del put[0]
    #put.remove('combe')			     
      check =1
    if check == 0:
     print('-',end='')
	  
				   