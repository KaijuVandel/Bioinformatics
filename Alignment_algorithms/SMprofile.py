from profile import *
from PSSM import *

def smprofile(S, gap, seq, residues,sc):
	'''A function that performs the local alignment of a sequence to a profile'''				
	f=frequency(S,residues)
	M=PSSM(seq,sc,residues,S)			
        F=[[0.0] * (len(f)+1) for i in range (0, len(seq)+1)]
	for i in range(1, len(seq)+1):	
		for j in range(1, len(f)+1):
			F[i][j]=max([F[i-1][j]+gap, F[i][j-1]+gap, F[i-1][j-1]+M[i-1][j-1],0.0])

	maxscore=0
	for i in range(1, len(seq)+1):	
		for j in range(1, len(f)+1):
			if F[i][j]>maxscore:
				maxscore=F[i][j]
	print F	
	print maxscore
				
		
#input examples
gap= -2
S=['ATCG', 'TATA', 'GTAC', 'GTCA', 'TATT', 'AATC','AGTC']
seq='TGTA'
residues=['A', 'T', 'C', 'G']
sc={('A','A'):10,('A','C'):-3, ('A','G'):-1, ('A','T'):-4,('G','A'):-1, ('G','G'):7, ('G','C'):-5, ('G','T'):-3, ('C','A'):-3, ('C','G'):-5,('C','C'):9, ('C','T'):0, ('T','A'):-4, ('T','G'):-3, ('T','C'):0, ('T','T'):8}


