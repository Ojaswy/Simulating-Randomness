from itertools import permutations 
import itertools 
from distfit import distfit
import numpy as np

val = []

#perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) 
#p =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
p =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#p = [1, 2, 3]
#perm = permutations([1, 2, 3]) 

length = len(p)

obj = {}
for i in range(1,length):
    obj[str(i)] = []


def numOfSubseq(arr, n): 
    i, inc_count, dec_count = 0, 0, 0; 
    max = [0]*n; 
    min = [0]*n; 
  
    # k2, k1 are used to store the 
    # count of max and min array 
    k1 = 0; 
    k2 = 0; 
  
    if (arr[0] < arr[1]): 
        min[k1] = 0; 
        k1 += 1; 
    else: 
        max[k2] = 0; 
        k2 += 1; 

    for i in range(1, n-1): 
        if (arr[i] < arr[i - 1] and arr[i] < arr[i + 1]): 
            min[k1] = i; 
            k1 += 1; 
          
        if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]): 
            max[k2] = i; 
            k2 += 1; 
  
    if (arr[n - 1] < arr[n - 2]): 
        min[k1] = n - 1; 
        k1 += 1; 
    else: 
        max[k2] = n - 1; 
        k2 += 1; 

    if (min[0] == 0): 
        inc_count = k2; 
        dec_count = k1 - 1; 
    else: 
        inc_count = k2 - 1; 
        dec_count = k1; 
      
    return (inc_count + dec_count)

	

for i in list(perm):
	val.append(numOfSubseq(i, length))

data = np.array(val, dtype = np.int64)

def CountFrequency(my_list): 
   count = {} 
   for i in my_list: 
    count[i] = count.get(i, 0) + 1
   return count

print(CountFrequency(val)) 

#DRISTRIBUTION FITTING

dist = distfit(smooth=10)

dist.fit_transform(data)

best_distr = dist.model
#print(best_distr)

dist.summary

dist.plot()
dist.plot_summary()


  

