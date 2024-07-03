#!/usr/bin/python
from __future__ import print_function
from collections import deque
import sys
import string
import math
import numpy as np

#10 bases
Delcim = 10
imax = 0 
total =[]
base  =[]
mylist =list()
secondlist =list()


def Change_Reverse(temp):
	c = 0
	rel =[]
	while temp >=1:	   
		dv = temp % 10
		temp = temp // 10  # only get int 
		value = Mulit(c)		
		base.append(value)
		total.append(dv)
		c=c+1
		imax = c	   
		     
	for n in range(0,imax):
	   rel.append(base[imax-1-n]*total[n])
	   #if n == imax-1:
	  # print(rel)
		
	su = sum(rel)
	print("Reverse Result =      " ,su)
#	print("OutPut Reverse Result = %.1d" % rel);	
	    #prod = map(lambda (a,b):a*b, zip(,))		
#		print("Reverse Result  = " ,rel)
#		for n in range(imax):
#			rel = rel + base[n]*total[imax-n] 
	
#	print("OutPut Reverse Result = %.1d" % rel);
	
#	print("base  -> " ,base)	 	 
#	print("total -> " ,total)		
	

def ClassfixIntValue(tmp1,tmp2,tmp3):
	cale =0
	check =0
	while tmp1 >= 1:
		#dv = tmp % 10
		cale += tmp1 % 10
		#total.append(dv)
		tmp1 = tmp1 // 10  # only get int

	while tmp2 >= 1:
		#dv = tmp % 10
		cale += tmp2 % 10
		#total.append(dv)
		tmp2 = tmp2 // 10  # only get int

	while tmp3 >= 1:
		#dv = tmp % 10
		cale += tmp3 % 10
		#total.append(dv)
		tmp3 = tmp3 // 10  # only get int

	# if cale >=10:
	# 	while cale >= 1:
	# 		check = 1
	# 		cv = cale %10
	# 		mylist.append(cv)
    #   		cale = cale //10

	# if check == 1:
	# 	final = 0
	# 	for k in range(0,len(mylist)):
	# 		final += mylist[k]
	# return final
	# if check == 1:
	# 	final = 0
	# 	for k in len(mylist):
	# 		final = final +mylist[k]
	#
	# 	return final
	return cale

def Mulit(n):
	num = 1				 
	for d in range(n):
		num = num * Delcim  #doing high Number	
	return num

def main():
	#a = input("Please input a birth day (Year Month Day): ")
	Final_Result_Magic_Num = 0
	Deep_Magic_Num =0
	chk =0
	chk2 =0
	y,m,d = map(int,input("Please input birth Y M D bellow \n").split())

	#LENGTH = len(a)
	#k = Mulit(a)
	#print("High Number is %.1d" % k)
	top = 0

	num1 = ClassfixIntValue(y,m,d)
	# for n in (len(total)):
	#    print("Th->"+top+ " "+ total[n] +"\n")
	#    top+=1

	#print("\n")

	#print("MyList -> "+mylist)
	# for k in range(0, len(mylist)):
	#     print("this->"+k+ "=" + mylist[k]+"\n")

	print("Number of MagicLife before =",num1)

	if num1 >=10:
		chk = 1
		while num1 !=0:
			cv = num1%10
			mylist.append(int(cv))
			num1 = num1 //10
		for i in range(len(mylist)):
			mylist[i] = int(mylist[i])
			Final_Result_Magic_Num += mylist[i]

		if Final_Result_Magic_Num >=10:
			chk2 = 1
			while Final_Result_Magic_Num !=0:
			 cc = Final_Result_Magic_Num %10
			 secondlist.append(int(cc))
			 Final_Result_Magic_Num /=10

			for i in range(len(secondlist)):
			 secondlist[i] = int(secondlist[i])
			 Deep_Magic_Num += secondlist[i]

	if chk:
		if chk2:
			print("Number of MagicLife Merge final ->",Deep_Magic_Num )
		else:
			print("Number of MagicLife Merge final ->", Final_Result_Magic_Num)
	else:
		print("Number of MagicLife Merge final ->", num1)

	#Change_Reverse(a)
	user = input("please input to quit...")
#	(raw_input for  PYTHON2.4 EDITION)
	#user = raw_input("please input to quit...")
	#k = input("Please Input Exit,TKS !")

if __name__ == '__main__':
	main()

