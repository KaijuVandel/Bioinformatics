def readmatrix(filename):
        f=open(filename)
        header=f.readline().rstrip().split()
        M={}
        for line in f:
                line.rstrip().split()
                label=line[0]
                print label
                for i in range(1,len(line)):
                        M[(label,header[i-1])]=float(line[i])
        return M
        f.close()
