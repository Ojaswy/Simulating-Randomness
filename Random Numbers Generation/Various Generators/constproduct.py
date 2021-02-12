import sys
import bisect

def const_product(a,b):
	ab = a*b
	val = ab // (10**(dig_count / 2))
	val = int(val % (10**dig_count) )
	return val

def const_product_list(a, b, length):
	lis = []
	for _ in range(length):
		v = const_product(a,b)
		a = v
		lis.append(v)
	return lis

if __name__ == '__main__':
	seed1 = 6217
	seed2 = 4978
	dig_count = len(str(seed1))
	lis = const_product_list(seed1, seed2, 50)

