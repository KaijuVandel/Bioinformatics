#!/usr/bin/env python
import sys

def fibo2(n):
	'''A function that given an integer number, returns the correspondant value of the Fibonacci series with time complexity 2n'''
	n=int(n)
	fib=[]
	for i in range(n+1):
		fib.append(i)
	fib[1]=1
	fib[2]=1
	for j in range(3,n+1):
		fib[j]=fib[j-1]+fib[j-2]
	return fib[n]

if __name__=="__main__":
	number=sys.argv[1]
	result=fibo2(number)
	print "the", number,"th number of the Fibonacci series is", result
