#!/usr/bin/env python
import sys

def min_value(x):
	'''This program takes in input a list of numbers and finds the minimum'''
	minscore=float(x[0])
	for number in x:
		number=float(number)
		if number<=minscore:
			minscore=number
	return minscore


if __name__=="__main__":
	series=sys.argv[1].split(',')
	result=min_value(series)
	print "The minimum value is", result
