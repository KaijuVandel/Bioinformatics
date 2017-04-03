#!/usr/bin/env python
import sys
import math

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

def pred_class(list_values,th=0.5):
	'''number higher than the threshold is considered as positive'''
	list_class=[]
	for value in list_values:
		if float(value[1])>th:
			list_class.append([int(value[0]),1])
		else:
			list_class.append([int(value[0]),0])
	return list_class
	
def get_accuracy(cmat):
	n=cmat[0][0]+cmat[1][1]+cmat[1][0]+cmat[0][1]
	return (cmat[0][0]+cmat[1][1])/float(n)

def get_mcc(cmat):
	#tp=cmat[1][1]
	#tn=cmat[0][0]
	#fp=cmat[1][0]
	#fn=cmat[0][1]
	mcc=0.0
	tot=(cmat[0][0]*cmat[1][1]-cmat[1][0]*cmat[0][1])
	d=math.sqrt((cmat[1][1]+cmat[1][0])*(cmat[1][1]+cmat[0][1])*(cmat[0][0]+cmat[1][0])*(cmat[0][0]+cmat[0][1]))
	if d>0:
		mcc=float(tot)/d
	return mcc

if __name__=='__main__':
	list_values=[]
	th=0.5
	f=open(sys.argv[1],'r')
	if len(sys.argv)>2: 
		th=float(sys.argv[2])
	for line in f:
		value=line.rstrip().split()
		list_values.append(value)
	list_preds=pred_class(list_values,th)
	mat=confusion_mat(list_preds)
	acc=get_accuracy(mat)
	mcc=get_mcc(mat)
	print 'CMAT: ',mat
	print 'ACC: ',acc
	print 'MCC: ',mcc

