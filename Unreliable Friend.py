def find(x1,y1,x2,y2,N,M,Mapel,count):
    if x1==x2 and y1==y2:
        return count
    if Mapel(x1,x2)=='~':
        count+=1
    if (x1!=0 and y1!=0) and (x1!=N and y1!=M) and (x1!=N and y1!=0) and (x1!=0 and y1!=M):
        if x1>x2:
            count = find(x1-1,y1,x2,y2,N,M,Mapel,count)
        elif x1<x2:
            count = find(x1+1,y1,x2,y2,N,M,Mapel,count)
        else:
            if y1>y2:
                count = find(x1,y1-1,x2,y2,N,M,Mapel,count)
            elif y1<y2:
                count = find(x1,y1+1,x2,y2,N,M,Mapel,count)
            
    elif (x1!=0 and y1!=0):
        _=0  
    elif (x1!=N and y1!=M):
        _=0
    elif (x1!=N and y1!=0):
        _=0
    elif (x1!=0 and y1!=M):
        _=0