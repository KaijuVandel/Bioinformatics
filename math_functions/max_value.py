#!/usr/bin/env python
import sys

def max_value(x):
	'''This program takes in input a list of numbers and finds the maximum'''
	maxscore=0.0
	for i in x:
		i=float(i)
		if i>maxscore:
			maxscore=i
	return maxscore

if __name__=="__main__":
	series=sys.argv[1].split(',')
	result=max_value(series)
	print "The maximum value is", result
	

		
