import copy
import sys
import time

def  goestoend(available,given,fuel,place,sum,path):
    stop = path[2]
    listed = True
    nofuel=False
    pathcopy = copy.deepcopy(path)
    placelist = {}
    placelist2 = {}
       
    
    if ('end',place) in given.keys():
            checktuple = ('end',place)
    elif (place,'end') in given.keys():
        checktuple = (place,'end')
    else:
        listed = False
    
    if listed:
        if fuel>=given[checktuple]:
            place = 'end'
            fuel -= given[checktuple]
            sum += given[checktuple]
            path[0].append(checktuple)
            path[1] += given[checktuple]#sum
            return path
        else:
            nofuel = True
            
    if nofuel or not listed:
        
        path = []
        for item,key in sorted([(value,key) for (key,value) in given.items()]):
            if key[0] == place:
                placelist[key] = item
            elif key[1] == place:
                placelist[key[1],key[0]] = item
                key = (key[1],key[0])
        
        for item,key in sorted([(value,key) for (key,value) in placelist.items()]):
            getin = True
            pathtemp = copy.deepcopy(pathcopy)
            for p in pathtemp[0]:
                if p[1] == key[1] or p[0] == key[1]:
                    getin = False
            if getin:
                if fuel >= item:
                    tempfuel = fuel
                    pathtemp[0].append(key)
                    tempfuel -= item
                    tempfuel += available[key[1]]
                    if tempfuel>100:
                        tempfuel = 100
                    pathtemp[1] += item
                    if key[1] == 'end':
                        pathtemp.append(stop)
                        path.extend(pathtemp)
                        if pathtemp[1]<stop:
                            stop = pathtemp[1]
                    else:
                        if pathtemp[1]<stop:           
                            if pathtemp[1]<stop:
                                g = dict(given)
                                for ite in pathtemp[0]:
                                    if ite in g:
                                        del g[ite]
                                    elif (ite[1],ite[0]) in g:
                                        del g[(ite[1],ite[0])]
                                pathtemp = goestoend(available,g,tempfuel,key[1],sum,pathtemp)
                                stop = pathtemp[2]
                                path.extend(pathtemp)
                else:
                    tempfuel = fuel
                    x = item -tempfuel
                    maxs = 0
                    maxtemp = 0
                    it = 0
                    itm=10000000
                    for key2,item2 in placelist.items():
                        if  ((available[key2[1]] + available[key2[0]] - 2*item2) > maxs):
                            maxtemp = available[key2[1]] + available[key2[0]] - 2*item2
                            mul = (item + item%(maxtemp+fuel))/(maxtemp+fuel)
                            mul = int(mul)
                            if mul>0:
                                if item2<item:
                                    itm = item2
                                    maxs = maxtemp
                                    it += 2*item2
                                    nod = key2
                    if maxs >0:
                        mul = (item + item%(maxs+fuel))/(maxs+fuel)
                        mul = int(mul)
                        if mul>0:             
                            for i in range(mul):
                                pathtemp[0].append(nod)
                                pathtemp[0].append(nod)
                                tempfuel -=it
                                if tempfuel>100:
                                    tempfuel = 100
                                pathtemp[1]+=it                                
                                tempfuel += 2*item
                                tempfuel = tempfuel + available[key[1]] + available[key[0]]
                                pathtemp[0].append(key)
                            if tempfuel>100:
                                tempfuel = 100
                            pathtemp[1] += item
                            if key[1] == 'end':
                                pathtemp.append(stop)
                                path.extend(pathtemp)
                                if pathtemp[1]<stop:
                                    stop = pathtemp[1]
                            else:
                                if pathtemp[1]<stop:
                                    if pathtemp[1]<stop:
                                        g = dict(given)
                                        for ite in pathtemp[0]:
                                            if ite in g:
                                                del g[ite]
                                            elif (ite[1],ite[0]) in g:
                                                del g[(ite[1],ite[0])]
                                        pathtemp = goestoend(available,g,tempfuel,key[1],sum,pathtemp)
                                        stop = pathtemp[2]
                                        path.extend(pathtemp)
        retpath = []
        mins = 10000
        for index,item in enumerate(path):
            
            if (index+2)%3 == 0:
                if item<mins and item!=0:
                    mins = item
                    retpath = path[index - 1]
        if mins == sys.maxsize:
            mins = 0
        return [retpath,mins,stop]

def checkfuel(available,given,fuel,place):
    path = [[],0,10000]
    path = goestoend(available,given,fuel,place,sum,path)
    if not path[0]:
        return "Impossible"
    else:
        return str(path[1])            

t = int(input())
start_time = time.time()
for i in range(t):
    esc=False
    sum = 0
    available = {}
    given = {}
    n = int(input())
    for j in range(n):
        i,f = [x for x in input().split()]
        available[i] = int(f)
    m = int(input())
    for k in range(m):
        i1,i2,fn = [x for x in input().split()]
        fn = int(fn)
        given[(i1,i2)] = fn
        if (fn >100 and ((i1=='end' and i2=='start') or (i1=='start' and i2=='end'))):
            esc=True
    if not esc:            
        fuel = available['start']
        place = 'start'
        print(checkfuel(available,given,fuel,place))        
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("Impossible")
        