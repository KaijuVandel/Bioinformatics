def average(x):
	'''This program takes in input a list of numbers and returns the average'''
	value=0.0
	for i in x:
		value=value+i
	value=float(value)/len(x)
	return value		
