#!/usr/bin/env python   
import sys

def average(x):
	'''This program takes in input a list of numbers and returns the average'''
	value=0.0
	for i in x:
		value=value+float(i)
	value=float(value)/len(x)
	return value

if __name__=="__main__":				    
	lista=sys.argv[1].split(',')
	print lista
	result=average(lista)
	print result
	
	
	
	
