#!/usr/bin/env python
import sys, math
from Bio.SubsMat import MatrixInfo

#This program takes in input a file with a multiple sequence alignment given in fasta format, then creates a profile based on it and computes the entropy

def get_fasta(filename):
	'''function to obtain a dictionary with the Uniprot ID as key and the sequence as value'''
	d={}
	with open(filename) as fp:      #it is the way python reads line by line not to fill all the ram
		for line in fp:
			line=line.rstrip()
			if line[0]=='>':
				unid=line.split('|')[1]
				continue
			d[unid]=d.get(unid,'')+line #if the line doesn't begin with > it add to the value the line and increases it
			#print unid, d[unid]
	return d

def get_entropy(aalist, aa='ACDEFGHIKLMNPQRSTVWY-'):
		'''function to calculate the profile for each position of the MSA and then the entropy.'''
		v=21*[0.0]
		l=len(aa)
		s=0.0
		for i in range(l):
			v[i]=aalist.count(aa[i])/float(len(aalist))
		for i in range(l):
			if v[i]>0.0:
				s=s-v[i]*math.log(v[i])
		return s,v

def get_score(aalist,subs,g=-1.0):
	'''The function calculates the score of the alignment'''
	#we simply calculate the score for all the possible pairs of sequences. 
	s=0.0
	n=len(aalist)
	for i in range(n):
		for j in range(i): #or from 0 to n-1. you are considering only one half of the possible alignments. 
			if aalist[i]=='-' and aalist[j]=='-': continue 
			if aalist[i]=='-' or aalist[j]=='-':
				s=s+g
			else:   
				try:
					s=s+subs[(aalist[i],aalist[j])] #if you use try you have to be 100% sure that it is true otherwise you always fall in except
				except:
					s=s+subs[(aalist[j],aalist[i])]
			#print aalist[i],aalist[j],s
				#i can try also with this
				#if subs.get((aalist[i], aalist[j],'')!='': 
					#s=s+subs[(aalist[i],aalist[j])]
					#continue
				#if subs.get((aalist[j], aalist[i],'')!='': s=s+subs[(aalist[j],aalist[i])]
					
					
				#if later on there is one gap i don't want to assign a negative score later
	return s

if __name__=="__main__":
	filename=sys.argv[1]
	#pos=int(sys.argv[2])-1
	d=get_fasta(filename)
	salign=d.values()
	stot=0.0
	n=len(salign[0])
	b62=MatrixInfo.blosum62
	for pos in range(n):
		pi=[i[pos] for i in salign]
		ent,prof=get_entropy(pi)
		s=get_score(pi,b62)
		stot=stot+s
		#print '%s\t%s\t%s' %(pos+1,''.join(pi),ent)
		#print pos+1, ''.join(pi), ent
		print pos+1, ''.join(pi), ent, s
	print "The total score is", stot
		
