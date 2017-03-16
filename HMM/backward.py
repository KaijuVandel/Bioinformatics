def backward(a,e,seq,states):
	'''implementation of the backward algorithm'''
	F=[[0.0 for i in range(len(seq)+2)] for s in states]
	F[-1][-1]=1
	for s in range(len(states)):
		F[s][-2]=F[s][-2]+a.get((states[s],states[-1]),0)
	for j in range(len(seq)-1,0,-1):
		for i in range(len(states)-2,0,-1):
			for w in range(len(states)):
				F[i][j]=F[i][j]+F[w][j+1]*a.get((states[i],states[w]),0)*e.get((states[w],seq[j]),0)
	for w in range(len(states)):
		F[0][0]=F[0][0]+F[w][1]*a.get((states[0],states[w]),0)*e.get((states[w],seq[0]),0)
	return F


#input examples

states=['B','Y','N','E'] #list of states

a={('B','Y'):0.2, ('B','N'):0.8, ('Y','Y'):0.7, ('Y','N'):0.2, ('N','Y'):0.1, ('N','N'):0.8, ('Y','E'):0.1, ('N','E'):0.1} #dictionary of transitions probabilities

e={('Y','A'):0.1, ('Y','G'):0.4, ('Y','C'):0.4, ('Y','T'):0.1, ('N','A'):0.25, ('N','G'):0.25, ('N','C'):0.25, ('N','T'):0.25} #dictionary of emission probabilities

seq='ATGCG' #example of sequence

