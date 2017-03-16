def variance2(x):
	'''This function takes in input a list of numbers and computes the variance using the definition of covariance of a random variable with itself'''
    lista=[]
    valore=0
    for value in x:
        valore=value**2
        lista.append(valore)
    avg2=average(lista)
    avg=(average(x))**2
    total=avg2-avg
    return total
