#!/usr/bin/env python
import sys

def fibo(n):
	'''The most simple function that finds the corresponding value of the Fibonacci series given a number''' 
	n=int(n)
	if n==1 or n==2:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)

if  __name__=="__main__":
	number=sys.argv[1]
	result=fibo(number)
	print "The", number, "th number of the Fibonacci series is", result
