#!/usr/bin/python
from __future__ import print_function
from collections import deque
import sys
import string
import math
from math import floor
import numpy as np
Delcim = 10

unique_list=[]

odd=[]
even=[]
result=[]

#case even = odd
#total=[2,41,13,10, 17,29 ,120 ,28]

# total=[2020,5,23,10,3,7,8,3,25,1]

#case 
total=[2020,5,23,10,12,27,2331,1,1148,3,3,25,66,12,66,1,27,2020,6,8,2331]

#case even < odd
#total=[2020,5,23,3,3,25,2,8,7,1,2021]

#case even > odd
#total=[22,15,17,90,131,188,2325,200,1000]

#total=[2020,5,23,10,3,7,8,44,25,1,5]

def min_array():
    min_temp = 0
    

def Control_Sort(nums):
    #nums.sort()
    odd_f = 0
    even_f = 0
    n = len(nums)
    for el in range(n):
        if nums[el] not in unique_list:
          unique_list.append(nums[el])
          
    for i in range(len(unique_list)):
    # We want the last pair of adjacent elements to be (n-2, n-1)
        j = i
        for j in range(len(unique_list) - 1):
            if unique_list[j] > unique_list[j+1]:
                    # Swap
                    unique_list[j], unique_list[j+1] = unique_list[j+1], unique_list[j]
 
    for kyo in range(len(unique_list)):
        if(unique_list[kyo]%2 == 0):
             even.append(unique_list[kyo])
             even_f = even_f +1 
        else:
             odd.append(unique_list[kyo])
             odd_f =  odd_f + 1
             
    diff = abs(len(even) - len(odd))
    if(diff == 0):
        Total_len = int(len(even) + len(odd))/int(2)
    else:
        Total_len = len(even) + len(odd)

    for iori in range(math.ceil(Total_len)):
         if(diff == 0):
            result.append(odd[iori])
            result.append(even[iori])
            # even = even[:iori] + even[iori+1 :]
            # odd = odd[:iori] + odd[iori+1 :]
            # even = even[:iori] + even[iori+1 :]
         elif(len(even) > len(odd)):
            if(iori < len(odd)):
                result.append(odd[iori])
                result.append(even[iori])
            else:
                if(iori <len(even)):
                    result.append(even[iori])
         elif(len(even) < len(odd)):
            if(iori < len(even)):
                result.append(odd[iori])
                result.append(even[iori])
            else:
                if(iori <len(odd)):
                    result.append(odd[iori])
         else:
             break
                
    return unique_list
	 
def Mulit(n):
	num = 1				 
	for d in range(n):
		num = num * Delcim  #doing high Number	
	return num
	

def main():
    # k = Mulit(3)
    k = Control_Sort(total)
    print("original Number of  = ",total)
    print("sort Number of  = ",k)
    print("odd of  = ",odd)
    print("even of  = ",even)
    print("odd/even result of  = ",result)
    #print("ak index = ",ak,end =' ')


if __name__ == '__main__':
     main()