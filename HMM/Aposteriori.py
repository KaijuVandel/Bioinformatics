def Aposteriori(a,e,seq,states):
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

Aposteriori(a,e,seq,states)			
