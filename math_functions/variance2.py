#!/usr/bin/env python
import sys

def average(x):
	tmp=0.0
	n=len(x)
	for number in x:
		tmp=tmp+float(number)
	result=tmp/n
	return result

def variance2(numbers):
	'''This function takes in input a list of numbers and computes the variance using the definition of covariance of a random variable with itself'''
    	lista=[]
    	valore=0.0
    	for value in numbers:
        	valore=float(value)**2
        	lista.append(valore)
    	avg2=average(lista)
    	avg=(average(numbers))**2
    	total=avg2-avg
    	return total


if __name__=="__main__":
	series=sys.argv[1].split(',')
	average(series)
	final=variance2(series)
	print "The variance is equal to", final
