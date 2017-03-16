def min_value(x):
	'''This program takes in input a list of numbers and finds the minimum'''
	minscore=x[0]
	for number in x:
		if number<=minscore:
			minscore=number
	return minscore
