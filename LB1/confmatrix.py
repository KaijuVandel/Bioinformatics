#!/usr/bin/env python
import sys

def confusion_mat(values_list): #lists of lists of 2 elements or of tuples of 2 elements
	'''I am calculating the number of cases and put them in the matrix'''
	cmat=[[0.0,0.0],[0.0,0.0]]
	for value in values_list:
		if value==[0,0]: #first value  real, second value predicted
			cmat[0][0]+=1 #it increments of 1
		elif value==[1,1]:
			cmat[1][1]+=1
		elif value==[0,1]:
			cmat[1][0]+=1 #because the matrix has in rows the prediction, and the gold in the colums so i have to invert (the matrix is composed of [TN,FN],[FP,TP]
		elif value==[1,0]:
			cmat[0][1]+=1
		else:
			pass
	return cmat

def get_accuracy(cmat):
	n=cmat[0][0]+cmat[1][1]+cmat[1][0]+cmat[0][1]
	return (cmat[0][0]+cmat[1][1])/float(n)

if __name__=='__main__':
	list_values=[]
	f=open(sys.argv[1],'r')
	for line in f:
		value=[int(i) for i in line.rstrip().split()]
		list_values.append(value)
	mat=confusion_mat(list_values)
	acc=get_accuracy(mat)
	print mat
	print acc


