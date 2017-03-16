
def nw(n, m, gap, subm):
	'''This algorithm performs the global alignment between two sequences given the sequences, the gap penalty and the substitution matrix'''						
        M=[[0.0] * (len(m)+1) for i in range (0, len(n)+1)]
        B=[[0.0] * (len(m)+1) for i in range (0, len(n)+1)]
	for i in range(0, len(n)+1):		
		M[i][0]= gap * i
		B[i][0]= "U"		
	for j in range(0, len(m)+1):		
		M[0][j]= gap * j
		B[0][j]= "L"	
	for j in range(1, len(m)+1):	
		for i in range(1, len(n)+1):
			M[i][j]=max(M[i-1][j]+gap, M[i][j-1]+gap, M[i-1][j-1]+subm[(n[i-1],m[j-1])])
			if M[i][j]==M[i-1][j-1]+subm[(n[i-1],m[j-1])]:
				B[i][j]='D'
			elif M[i][j]==M[i][j-1]+gap:
				B[i][j]='L'
			else:
				B[i][j]='U'
	i = len(n)
	j = len(m)
	score=M[i][j]
	Al1 = ""
	Al2 = ""
	while i>0 and j>0:
		if B[i][j]=='D':
			i=i-1
			j=j-1
			Al1=n[i]+Al1
			Al2=m[j]+Al2
		elif B[i][j]=='U':
			i=i-1
			Al1=n[i]+Al1
			Al2='-'+Al2
		else:
			j=j-1
			Al1='-'+Al1
			Al2=m[j]+Al2
	while i>0:
		i=i-1
		Al1=n[i]+Al1
		Al2='-'+Al2
	while j>0:
		j=j-1
		Al1='-'+Al1
		Al2=m[j]+AL2
		
	
	seq=''
	for i in range(len(Al1)):
		if Al1[i]==Al2[i]:
			seq=seq+'|'
		else:
			if Al2[i]=='-' or Al1[i]=='-':
				seq=seq+'.'
			else:
				seq=seq+':'
			
		
		
	return score		
	return Al1
	return seq
	return Al2





