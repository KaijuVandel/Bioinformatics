def Smith(s1,s2,sub,gap):
	'''This function performs the local alignment between 2 sequences, given the sequences, the substitution matrix and the gap penalty'''
	F=[[0.0 for i in range(len(s1)+1)] for i in range(len(s2)+1)]
	B=[[0.0 for i in range(len(s1)+1)] for i in range(len(s2)+1)]
	for i in range(1,len(s2)+1):
		for j in range(1,len(s1)+1):
			F[i][j]=max([F[i-1][j-1]+sub[(s2[i-1],s1[j-1])],F[i-1][j]+gap, F[i][j-1]+gap, 0.0])
			if F[i][j]==F[i-1][j-1]+sub[(s2[i-1],s1[j-1])]:
				B[i][j]='D'
			elif F[i][j]==F[i-1][j]+gap:
				B[i][j]='U'
			elif F[i][j]==F[i][j-1]+gap:
				B[i][j]='L'
			else:
				B[i][j]='0'
	
	score=F[1][1]	
	for i in range(1,len(s2)+1):
		for j in range(1, len(s1)+1):
			if F[i][j]>=score:
				score=F[i][j]
				n=i
				m=j
	al1=''
	al2=''
	while F[n][m]>0:
		if B[n][m]=='D':
			m=m-1
			n=n-1			
			al1=s1[m]+al1
			al2=s2[n]+al2
		elif B[n][m]=='U':
			m=m-1
			n=n
			al1=s1[m]+al1
			al2='-'+al2
		elif B[n][m]=='L':
			m=m
			n=n-1
			al1='-'+al1
			al2=s2[n]+al2
	return score
	return al1
	return al2
	


