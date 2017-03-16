def backward(a,e,seq,states):
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
	print F











states=['s1','s2','s3','s4']
a={('s1','s2'):0.2, ('s1','s3'):0.8, ('s2','s2'):0.7, ('s2','s3'):0.2, ('s3','s2'):0.1, ('s3','s3'):0.8, ('s2','s4'):0.1, ('s3','s4'):0.1}
e={('s2','A'):0.1, ('s2','G'):0.4, ('s2','C'):0.4, ('s2','T'):0.1, ('s3','A'):0.25, ('s3','G'):0.25, ('s3','C'):0.25, ('s3','T'):0.25}

seq='ATGCG'

backward(a,e,seq,states)
