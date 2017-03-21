#!/usr/bin/env python
import sys

def fibo3(n):
	'''A function that given an integer number, returns the corresponding value in Fibonacci's series, with time complexity 4n-4'''
	n=int(n)
	if n==1 or n==2:
		return 1
	else:
		F_nm1=1
		F_nm2=1
		for i in range (3,n+1):
			F_n=F_nm1 + F_nm2
			F_nm2=F_nm1
			F_nm1=F_n
	return F_n

if __name__=="__main__":
	number=sys.argv[1]
	result=fibo3(number)
	print "The", number, "th number of the Fibonacci series is", result
