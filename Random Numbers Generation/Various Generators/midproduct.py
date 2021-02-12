import sys
import bisect

def mid_product(a,b):
	ab = a*b
	val = ab // (10**(dig_count / 2))
	val = int(val % (10**dig_count) )
	return val

def mid_product_list(a, b, length):
	lis = []
	for _ in range(length):
		v = mid_product(a,b)
		a = b
		b = v
		lis.append(v)
	return lis

if __name__ == '__main__':
	seed1 = 7362
	seed2 = 9138
	dig_count = len(str(seed1))
	lis = mid_product_list(seed1, seed2, 50)

