from profile import *

def PSSM(seq,sc,residues,S):
	'''This function return a PSSM given a sequence, a substitution matrix, a list of possible residues or nucleotides and a multiple alignment'''
	f=profile(S,residues)
	M=[]
	for i in range(len(seq)):
		a=seq[i]
		tmp=[]
		for j in range(len(f)):
			acc=0.0
			for b in residues:
				acc=acc+f[j].get(a,0)*sc.get((a,b),0)
			tmp.append(acc)
		M.append(tmp)
	return M

#input examples
seq='ATCGTCAT'
residues=['A','C','T','G']
S=['AATACTGA','AACGGTGA','TATGCAAT','CCGCCACT'] #the sequences must have the same length

f=[{'A': 0.5, 'C': 0.25, 'T': 0.25}, {'A': 0.75, 'C': 0.25}, {'C': 0.25, 'T': 0.5, 'G': 0.25}, {'A': 0.25, 'C': 0.25, 'G': 0.5}, {'C': 0.75, 'G': 0.25}, {'A': 0.5, 'T': 0.5}, {'A': 0.25, 'C': 0.25, 'G': 0.5}, {'A': 0.5, 'T': 0.5}]


sc={('A','A'):2,('A','C'):-1, ('A','G'):1, ('A','T'):-1,('G','A'):1, ('G','G'):2, ('G','C'):-1, ('G','T'):-1, ('C','A'):-1, ('C','G'):-1,('C','C'):2, ('C','T'):1, ('T','A'):-1, ('T','G'):-1, ('T','C'):1, ('T','T'):2} #substitution matrix

