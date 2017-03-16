def forward(a,e,seq,states):
	F=[[0.0 for i in range(len(seq)+2)] for s in states]
	F[0][0]=1
	for j in range(1,len(seq)+1):
		for i in range(len(states)):
			for w in range(len(states)):
				F[i][j]=F[i][j]+F[w][j-1]*a.get((states[w], states[i]),0)
			F[i][j]=F[i][j]*e.get((states[i],seq[j-1]),0)
	for w in range(len(states)):
		F[-1][-1]=F[-1][-1]+F[w][-2]*a.get((states[w],states[-1]),0)
	print F






states=['s1','s2','s3','s4']
a={('s1','s2'):0.2, ('s1','s3'):0.8, ('s2','s2'):0.7, ('s2','s3'):0.2, ('s3','s2'):0.1, ('s3','s3'):0.8, ('s2','s4'):0.1, ('s3','s4'):0.1}
e={('s2','A'):0.1, ('s2','G'):0.4, ('s2','C'):0.4, ('s2','T'):0.1, ('s3','A'):0.25, ('s3','G'):0.25, ('s3','C'):0.25, ('s3','T'):0.25}

seq='ATGCG'

forward(a,e,seq,states)
