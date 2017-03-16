def max_value(x):
	'''This program takes in input a list of numbers and finds the maximum'''
	maxscore=0.0
	for number in x:
		if number>=maxscore:
			maxscore=number
	return maxscore
		
