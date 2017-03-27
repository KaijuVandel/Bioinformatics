#!/usr/bin/env python
import sys, math, random
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

def get_score(aalist,subs,g=0.0):
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
				#if subs.get((aalist[i], aalist[j],0)!=0: 
					#s=s+subs[(aalist[i],aalist[j])]
				#elif subs.get((aalist[j], aalist[i],0)!=0:
					#s=s+subs[(aalist[j],aalist[i])]
				#else:
					#pass  #pass is a command to skip directly to the following lines, while continue would go back to the first loop
				#if subs.get((aalist[j], aalist[i],'')!='': s=s+subs[(aalist[j],aalist[i])]
					
					
				#if later on there is one gap i don't want to assign a negative score later
	return s

def score_ali(seqs, matrix):
	'''calculates the total score'''
	stot=0.0
	for pos in range(len(seqs[0])):
		pi=[i[pos] for i in seqs]
		s=get_score(pi,matrix)
		stot=stot+s
		#print pos+1, ''.join(pi), ent
		#print pos+1, ''.join(pi), ent, s
	return stot
	




def shuffle_seq(seq):
	'''A function to randomize the sequence'''
	rseq=''
	lseq=list(seq)
	random.shuffle(lseq)
	rseq=''.join(lseq)
	return rseq

def random_align(seqs):
	'''randomize the MSA'''
	rali=[]
	n=len(seqs)
	for i in range(n):
		seq=seqs[i]
		if i%2==0:
			rali.append(shuffle_seq(seq))
		else:
			rali.append(seq)
	return rali



if __name__=="__main__":
	filename=sys.argv[1]
	#pos=int(sys.argv[2])-1
	d=get_fasta(filename)
	salign=d.values()
	stot=0.0
	n=len(salign[0])
	b62=MatrixInfo.blosum62
	stot=score_ali(salign,b62)
	for pos in range(len(n)):
		pi=[i[pos] for i in salign]
		ent,prof=get_entropy(pi)
	vscore=[]
	for i in range(100): #repeat 100 times to make it more random
		rali=random_align(salign)
		rtot=score_ali(rali,b62)
		vscore.append(rtot)
	print vscore
	print 'The alignment score is', stot
