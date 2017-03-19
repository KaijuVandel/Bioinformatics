import sys

def readmatrix(filename):
	'''A function to read a matrix from a file'''
        f=open(filename)
        header=f.readline().rstrip().split()
        M={}
        for line in f:
                line=line.rstrip().split()
                label=line[0]
                for i in range(1,len(line)):
                        M[(label,header[i-1])]=float(line[i])
        return M
        f.close()

if __name__=="__main__":
	filepath=sys.argv[1]
	matrix=readmatrix(filepath)
	print matrix
