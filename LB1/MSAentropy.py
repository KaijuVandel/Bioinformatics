#!/usr/bin/env python
import sys, math

#This program takes in input a file with a multiple sequence alignment given in fasta format, then creates a profile based on it and computes the entropy

def get_fasta(filename):
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
		v=21*[0.0]
		l=len(aa)
		s=0.0
		for i in range(l):
			v[i]=aalist.count(aa[i])/float(len(aalist))
		for i in range(l):
			if v[i]>0.0:
				s=s-v[i]*math.log(v[i])
		return s,v




if __name__=="__main__":
	filename=sys.argv[1]
	#pos=int(sys.argv[2])-1
	d=get_fasta(filename)
	salign=d.values()
	n=len(salign[0])
	for pos in range(n):
		pi=[i[pos] for i in salign]
		ent,prof=get_entropy(pi)
		print '%s\t%s\t%s' %(pos+1,''.join(pi),ent)
		
