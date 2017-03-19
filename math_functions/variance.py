#!/usr/bin/env python
import sys

def average(x):
	tmp=0.0
	n=len(x)
	for number in x:
		tmp=tmp+float(number)
	result=tmp/n
	return result

def variance(numbers):
	'''This function takes in input a list of number and computes the variance'''
	n=len(numbers)
    	total=0.0
	avg=average(numbers)
   	for value in numbers:
		value=float(value)
       		total=total + (value-avg)**2
   	total=total/(n-1)
    	return total


if __name__=="__main__":
	series=sys.argv[1].split(',')
	average(series)
	final=variance(series)
	print "The variance is equal to", final
