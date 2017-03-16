
def fibo(n):
	'''A function that finds the corresponding value of the Fibonacci series given a number''' 
	if n==1 or n==2:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)
