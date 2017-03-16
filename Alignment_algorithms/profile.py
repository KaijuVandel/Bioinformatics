def profile(S,residues):
	'''This function finds the frequency of each residue in each position in the sequences'''
	F=[]
	for i in range(len(S[0])):
		D={}
		for seq in S:
			D[seq[i]]=D.get(seq[i],0)+1
		for k in D:
			if k in residues:
				D[k]=float(D[k])/len(S)
		F.append(D)
	return F

#input examples
seq='ATCGTCAT'
residues=['A','C','T','G']
S=['AATACTGA','AACGGTGA','TATGCAAT','CCGCCACT'] #the sequences must have the same length



