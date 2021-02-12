import sys
import bisect

def mid_square(n):
	sqr = n**2
	val = sqr // (10**(dig_count / 2))
	val = int(val % (10**dig_count) )
	return val

def mid_square_list(n, length):
	lis = []
	a = n
	for _ in range(length):
		lis.append(a)
		a = mid_square(a)
	return lis

if __name__ == '__main__':
	i = 5928
	dig_count = len(str(i))
	lis = mid_square_list(i, 50)

print(lis)
