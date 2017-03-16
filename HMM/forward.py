def forward(a,e,seq,states):
	'''Implementation of the forward algorithm'''
	F=[[0.0 for i in range(len(seq)+2)] for s in states]
	F[0][0]=1
	for j in range(1,len(seq)+1):
		for i in range(len(states)):
			for w in range(len(states)):
				F[i][j]=F[i][j]+F[w][j-1]*a.get((states[w], states[i]),0)
			F[i][j]=F[i][j]*e.get((states[i],seq[j-1]),0)
	for w in range(len(states)):
		F[-1][-1]=F[-1][-1]+F[w][-2]*a.get((states[w],states[-1]),0)
	return F


#input examples

states=['B','Y','N','E'] #list of states

a={('B','Y'):0.2, ('B','N'):0.8, ('Y','Y'):0.7, ('Y','N'):0.2, ('N','Y'):0.1, ('N','N'):0.8, ('Y','E'):0.1, ('N','E'):0.1} #dictionary of transitions probabilities

e={('Y','A'):0.1, ('Y','G'):0.4, ('Y','C'):0.4, ('Y','T'):0.1, ('N','A'):0.25, ('N','G'):0.25, ('N','C'):0.25, ('N','T'):0.25} #dictionary of emission probabilities

seq='ATGCG' #example of sequence
