def forward(a,e,seq,states):
	F=[[0.0 for i in range(len(seq)+2)] for s in states]
	F[0][0]=1
	for s in range(len(states)):
		for w in range(len(states)):
			F[s][1]=F[s][1]+F[w][0]*a.get((states[w],states[s]),0)*e.get((states[s],seq[0]),0)
	for j in range(2,len(seq)+1):
		for i in range(len(states)):
			for w in range(len(states)):
				F[i][j]=F[i][j]+F[w][j-1]*a.get((states[w], states[i]),0)
			F[i][j]=F[i][j]*e.get((states[i],seq[j-1]),0)
	for w in range(len(states)):
		F[-1][-1]=F[-1][-1]+F[w][-2]*a.get((states[w],states[-1]),0)
	return F


states=['B','Y','N','E']
a={('B','Y'):0.2, ('B','N'):0.8, ('Y','Y'):0.7, ('Y','N'):0.2, ('N','Y'):0.1, ('N','N'):0.8, ('Y','E'):0.1, ('N','E'):0.1}
e={('Y','A'):0.1, ('Y','G'):0.4, ('Y','C'):0.4, ('Y','T'):0.1, ('N','A'):0.25, ('N','G'):0.25, ('N','C'):0.25, ('N','T'):0.25}

seq='ATGCG'

forward(a,e,seq,states)

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
	return F




states=['B','Y','N','E']
a={('B','Y'):0.2, ('B','N'):0.8, ('Y','Y'):0.7, ('Y','N'):0.2, ('N','Y'):0.1, ('N','N'):0.8, ('Y','E'):0.1, ('N','E'):0.1}
e={('Y','A'):0.1, ('Y','G'):0.4, ('Y','C'):0.4, ('Y','T'):0.1, ('N','A'):0.25, ('N','G'):0.25, ('N','C'):0.25, ('N','T'):0.25}

seq='ATGCG'

backward(a,e,seq,states)



def posteriori(a,e,seq,states):
	B=backward(a,e,seq,states)
	F=forward(a,e,seq,states)
	M=[[0.0 for i in range(len(seq)+2)] for s in states]
	#for s in range(len(states)):
	#	M[s][0]=float(F[s][0]*B[s][0])/F[-1][-1]
	for j in range(len(seq)+2):
		for i in range(len(states)):
			M[i][j]=float(F[i][j]*B[i][j])/F[-1][-1]
			
	#for s in range(len(states)):
	#	M[s][-1]=float(F[s][-1]*B[s][-1])/F[-1][-1]
	
	mao='B'
	for j in range(1,len(seq)+1):
		mas=0.0
		for i in range(1,len(states)-1):
			if M[i][j]>mas:
				mas=M[i][j]
				p=i
				q=j
		mao=mao+states[p]	
	mao=mao+states[-1]	
	print mao
	print M
	

			

states=['B','Y','N','E']
a={('B','Y'):0.2, ('B','N'):0.8, ('Y','Y'):0.7, ('Y','N'):0.2, ('N','Y'):0.1, ('N','N'):0.8, ('Y','E'):0.1, ('N','E'):0.1}
e={('Y','A'):0.1, ('Y','G'):0.4, ('Y','C'):0.4, ('Y','T'):0.1, ('N','A'):0.25, ('N','G'):0.25, ('N','C'):0.25, ('N','T'):0.25}

seq='ATGCG'

posteriori(a,e,seq,states)			
	


























states=['B','Y','N','E']
a={('B','Y'):0.2, ('B','N'):0.8, ('Y','Y'):0.7, ('Y','N'):0.2, ('N','Y'):0.1, ('N','N'):0.8, ('Y','E'):0.1, ('N','E'):0.1}
e={('Y','A'):0.1, ('Y','G'):0.4, ('Y','C'):0.4, ('Y','T'):0.1, ('N','A'):0.25, ('N','G'):0.25, ('N','C'):0.25, ('N','T'):0.25}

seq='ATGCG'
