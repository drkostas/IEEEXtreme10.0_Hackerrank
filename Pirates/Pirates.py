def find(x1,y1,x2,y2,N,M,Mapelsec,count):
    
    print(x1,y1,x2,y2,count)
    
    if Mapelsec[x1][y1]=='~':
        count+=1
    Mapelsec[x1][y1]='X'
    if (x1==x2 and y1==y2):
        return count
    elif x1>x2 and Mapelsec[x1-1][y1]!='~':
        if Mapelsec[x1-1][y1]!='X':
            count = find(x1-1,y1,x2,y2,N,M,Mapelsec,count)
            return count
    elif x1<x2 and Mapelsec[x1+1][y1]!='~':
        if Mapelsec[x1+1][y1]!='X':
            count = find(x1+1,y1,x2,y2,N,M,Mapelsec,count)
            return count
    elif y1>y2 and Mapelsec[x1][y1-1]!='~' :
        if Mapelsec[x1][y1-1]!='X':
            count = find(x1,y1-1,x2,y2,N,M,Mapelsec,count)
            return count
    elif y1<y2 and Mapelsec[x1][y1+1]!='~':
        if Mapelsec[x1][y1+1]!='X':
            count = find(x1,y1+1,x2,y2,N,M,Mapelsec,count)
            return count
    else:
        Mapelsec[x1-1][y1]='0'
        Mapelsec[x1+1][y1]='0'
        Mapelsec[x1][y1-1]='0'
        Mapelsec[x1][y1+1]='0'
        count = find(x1,y1,x2,y2,N,M,Mapelsec,count)
        return count
    
        

x1 = []
x2 = []
y1 = []
y2 = []

N,M,Q = [int(x) for x in input().split()]
Mapel=[[0 for x in range(N)] for y in range(M)] 

for i in range(N):
    line = input()
    Mapel[i] = list(line)
    

for i in range(Q):
    x1,y1,x2,y2=[int(x) for x in input().split()] 
    x1-=1
    x2-=1
    y1-=1
    y2-=1
for i in range(Q):
    Mapelsec = Mapel[:]
    if Mapelsec[x1][y1]=='~':
        count =1
    else:
        count = 0
    count = find(x1,y1,x2,y2,N,M,Mapelsec,count)
    
    print(count)