#!/usr/bin/env python   
#the system understands that the script is using python  or /usr/bin/python
import sys #from the input from command line
import numpy as np
from Bio.SVDSuperimposer import SVDSuperimposer

#This program perfoms the superimposition between 2 structures, taking the atoms coordinates from the PDB files and calculating the RMSD. 

def get_calpha(pdbfile,chain,rlist,atom="CA"): #rlist = residues list. return a list of 3d vectors. I can use now with 3 or 4 variables. if i use 4 the fourth would be 'CA', you automatically initialize it if it not defined.
	vca=[]
	fh=open(pdbfile,'r')
	for line in fh:
		line=line.rstrip()
		if line[:4]!="ATOM": continue
		if line[21]!=chain: continue 
		if line[12:16].strip()!=atom: continue
		n=line[22:26].strip()
		x=float(line[32:38])
		y=float(line[38:46])
		z=float(line[46:54])
		if n in rlist: 
			#print n,[x,y,z]
			vca.append([x,y,z])
	return vca

def run_sup3d(coord1,coord2):
	sup=SVDSuperimposer()
	sup.set(np.array(coord1),np.array(coord2)) #set is setting the group of coordinates because i have initialized SVD, it is empty
	sup.run() #superimpose the coordinates, run fa tutto, il resto sol per stampare le coordinate. faccio l'rmsd sulle coordinate di vca1 e vc2 dopo trasformazione
	rmsd=sup.get_rms()
	rot,tran=sup.get_rotran() #shows the matrix of rotation and vector for translation
	tcoord=sup.get_transformed()
	print rmsd
	print rot
	print tran
	print tcoord #you obtain the set of coordinates to be superimposable to the se 1, so the set of coordinates after transformation. 
	return 



	                              
                          
if __name__=="__main__":
	atom='CA'  				    #it defines how the command is runnig. if you are importing, this will not do anything
	pdb1=sys.argv[1]
	pdb2=sys.argv[2]
	ch1=sys.argv[3]
	ch2=sys.argv[4]
	rlist1=sys.argv[5].split(',')
	rlist2=sys.argv[6].split(',')
	if len(sys.argv)>7: atom=sys.argv[7]
	vca1=get_calpha(pdb1,ch1,rlist1,atom)
	vca2=get_calpha(pdb2,ch2,rlist2,atom)
	if len(vca1)!=len(vca2):                  #in order not to make the superimposition crash  the sets must be of the the same len
		print >> sys.stderr, "ERROR: Incorrect number of elements."
		sys.exit(1) # i assign a number to the different types of errors. 0 is the correct exit
	run_sup3d(vca1,vca2)	
	print vca1
	print vca2
