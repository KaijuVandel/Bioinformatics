def viterbi(a,e,seq,states):
	F=[[0.0 for i in range(len(seq)+2)] for s in states]
	F[0][0]=1
	ptr=[[0 for i in range(len(seq)+2)] for s in states]
	for s in range(len(states)):
		F[s][1]=a.get((states[0],states[s]),0)*e.get((states[s],seq[0]),0)
		ptr[s][1]=0			
	for j in range(2,len(seq)+1):
		for i in range(1,len(states)-1):
			for w in range(1,len(states)-1):
				F[i][j]=max([F[w][j-1]*a.get((states[w],states[i]),0)])
				#va implementato meglio il massimo
				ptr[i][j]=w
			F[i][j]=F[i][j]*e.get((states[i],seq[j-1]),0)

	for w in range(len(states)-1):
		F[-1][-1]=max([F[w][-2]*a.get((states[w],states[-1]),0)])
	        ptr[-1][-1]=w
	

	back=''
	j=len(seq)+1
	i=len(states)-1
	while j>0 and i>0:
		back=states[ptr[i][j]]+back
		i=ptr[i][j]		
		j=j-1

	back=back+states[-1]
		
	print F
	print ''
	print seq
	print back
				
			









states=['B','Y','N','E']
a={('B','Y'):0.2, ('B','N'):0.8, ('Y','Y'):0.7, ('Y','N'):0.2, ('N','Y'):0.1, ('N','N'):0.8, ('Y','E'):0.1, ('N','E'):0.1}
e={('Y','A'):0.1, ('Y','G'):0.4, ('Y','C'):0.4, ('Y','T'):0.1, ('N','A'):0.25, ('N','G'):0.25, ('N','C'):0.25, ('N','T'):0.25}

seq='ATGCG'

viterbi(a,e,seq,states)
