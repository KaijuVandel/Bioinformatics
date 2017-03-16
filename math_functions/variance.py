def variance(x):
	'''This function takes in input a list of number and computes the variance'''
    avg=average(x)
    n=len(x)
    total=0
    for value in x:
        total=total + (value-avg)**2
    total=total/(n-1)
    return total
    
