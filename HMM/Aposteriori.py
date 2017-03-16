def Aposteriori(a,e,seq,states):
	'''Implementation of the A posteriori decoding algorithm'''
	B=backward(a,e,seq,states)
	F=forward(a,e,seq,states)
	M=[[0.0 for i in range(len(seq)+2)] for s in states]
	for j in range(len(seq)+2):
		for i in range(len(states)):
			M[i][j]=float(F[i][j]*B[i][j])/F[-1][-1]
	
	back='B'
	for j in range(1,len(seq)+1):
		mas=0.0
		for i in range(1,len(states)-1):
			if M[i][j]>mas:
				mas=M[i][j]
				p=i
				q=j
		back=back+states[p]	
	back=back+states[-1]	
	return back
	return M

#input examples

states=['B','Y','N','E']   #list of states, begin (B) and end (E) states are included

a={('B','Y'):0.2, ('B','N'):0.8, ('Y','Y'):0.7, ('Y','N'):0.2, ('N','Y'):0.1, ('N','N'):0.8, ('Y','E'):0.1, ('N','E'):0.1}
#dictionary of trnasitions probabilities between the states

e={('Y','A'):0.1, ('Y','G'):0.4, ('Y','C'):0.4, ('Y','T'):0.1, ('N','A'):0.25, ('N','G'):0.25, ('N','C'):0.25, ('N','T'):0.25}
#dictionary of the emissions probabilities of the characters

seq='ATGCG' #example of a sequence
