def nwg(n, m, gap, subm):
	'''This function performs the global alignment without end-gap-penalties between two sequences, given the sequences, the gap penalty and the substitution matrix''' 			
        M=[[0.0] * (len(m)+1) for i in range (0, len(n)+1)]
        B=[[0.0] * (len(m)+1) for i in range (0, len(n)+1)]
	for i in range(1, len(n)+1):		
		for j in range(1, len(m)+1):
			M[i][j]=max([M[i-1][j]+gap, M[i][j-1]+gap, M[i-1][j-1]+subm[(n[i-1],m[j-1])]])
			if M[i][j]==M[i-1][j-1]+subm[(n[i-1],m[j-1])]:
				B[i][j]='D'
			elif M[i][j]==M[i][j-1]+gap:
				B[i][j]='L'
			else:
				B[i][j]='U'


	p=len(n)
	q=len(m)
	for i in range(1, len(n)+1):	
		for j in range(1, len(m)+1):
   			mas=max([M[p][j], M[i][q]])
			if M[i][j]==mas:
				mas=M[i][j]
				p=i
				q=j
				
			
        Al1 = ""
	Al2 = ""
	while p>0 and q>0:
		if B[p][q]=='D':
			p=p-1
			q=q-1
			Al1=n[p]+Al1
			Al2=m[q]+Al2
		elif B[p][q]=='U':
			p=p-1
			Al1=n[p]+Al1
			Al2='-'+Al2
		else:
			q=q-1
			Al1='-'+Al1
			Al2=m[q]+Al2
	while p>0:
		p=p-1
		Al1=n[p]+Al1
		Al2='-'+Al2
	while q>0:
		q=q-1
		Al1='-'+Al1
		Al2=m[q]+Al2
	
	seq=''
	for i in range(len(Al1)):
		if Al1[i]==Al2[i]:
			seq=seq+'|'
		else:
			if Al1[i]=='-' or Al2[i]=='-':
				seq=seq+'.'
			else:
				seq=seq+':'
		
		
			
			
	return mas
	return Al1
	return seq
	return Al2
        

