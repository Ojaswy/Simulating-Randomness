from itertools import combinations 
import math 
import numpy as np
import random

def multiplicativeCongruentialMethod(Xo, m, a, lis, noOflis): 

	# Initialize the seed state 
	lis[0] = Xo 

	# Traverse to generate required 
	# numbers of random numbers 
	for i in range(1, noOflis): 
		
		# Follow the linear congruential method 
		lis[i] = (lis[i - 1] * a) % m 
#Xo = random.randrange(10, 100, 3)
#m = random.randrange(10, 100, 3)
#a = random.randrange(10, 100, 2)
Xo = 3
m = 64
a = 89

noOflis = 200
lis = [0] * (noOflis) 
multiplicativeCongruentialMethod(Xo, m, a, lis, noOflis) 

# RELATIVE PRIME
def gdc(x,y):
    t =0
    while (y != 0):
        t = x
        x = y 
        y = t % y
    return x;

def relativePrime( x,y):
    z = gdc(x,y)
    if z == 1:
        return True
    else:
        return False

rp = 0
comb = combinations(lis, 2)
for i in list(comb): 
	if relativePrime(i[0],i[1]) == True:
		rp = rp + 1

# CYCLE LENGTH
'''
values = np.array(lis)
for i in range(len(lis)):
	searchval = lis[i]
	ii = np.array(np.where(values == searchval)[0])
	ii.tolist()
	if len(ii) >= 2:	
		l = ii[1] - ii[0]
		break
'''
values = np.array(lis)
searchval = lis[0]
ii = np.array(np.where(values == searchval)[0])
ii.tolist()
if len(ii) >= 2:	
	l = ii[1] - ii[0]
else:
	l = 0


# PRIMITIVE NUMBER
def getSum(n): 
    sum = 0
    for i in range(1, int(math.sqrt(n) + 1)): 
        if (n % i == 0): 
            if (n // i == i): 
                sum = sum + i 
            else: 
                sum = sum + i 
                sum = sum + (n // i) 
    return sum

def checkAbundant(n): 
    if (getSum(n) - n > n): 
        return True
    return False
  
def isDeficient(n): 
    if (getSum(n) < (2 * n)): 
        return True
    return False

def checkPrimitiveAbundant(num): 
    if not checkAbundant(num): 
        return False
    for i in range(2, int(math.sqrt(num) + 1)): 
        if (num % i == 0 and i != num): 
            if (i * i == num): 
                if (not isDeficient(i)): 
                    return False
            elif (not isDeficient(i) or 
                  not isDeficient(num // i)):  
                return False
    return True
 

for i in lis:
	if (checkPrimitiveAbundant(i)):
		primitive = i
		break
	else:
		primitive = 0
		break

# OUTPUT
#print(lis)
print("Seed:", Xo,",", "m:", m,",", "a:", a)
print("Number of Values Generated:", noOflis)
if l == 0:
	print("No repetition found. Cycle does not exist.")
else:
	print("Cycle Length:", l)
print("Number of Relative Primes:", rp)
if primitive == 0:
	print("Primitive Number Not Found")

else:
	print("Primitive Number:", primitive)
















