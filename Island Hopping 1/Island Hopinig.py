import copy
import sys
import time

def  goestoend(available,given,fuel,place,sum,path,depth):
    stop = path[2]
    print(depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth)
    print("MPIKE STI SINARTISI goestoend me stop = ",stop)
    print("Finding path to end...")
    listed = True
    nofuel=False
    pathcopy = copy.deepcopy(path)
    print("PATHCOPY: ",pathcopy)
    placelist = {}
    placelist2 = {}
       
    
    if ('end',place) in given.keys():
            checktuple = ('end',place)
    elif (place,'end') in given.keys():
        checktuple = (place,'end')
    else:
        listed = False
        print("0To ",place,"den exei antistoixhsh sto end")
    
    if listed:
        print("0To ",place," exei antistoixhsh sto end")
        if fuel>=given[checktuple]:
            print("0Paei apo  ",place,' sto end')
            place = 'end'
            fuel -= given[checktuple]
            sum += given[checktuple]
            print("0Diathesima kausima",fuel)
            path[0].append(checktuple)
            path[1] += given[checktuple]#sum
            print("0path: ",path)
            return path
        else:
            nofuel = True
            
            print("0Omws den exei arketa kausima")
            print("0Sigekrimena tou leipoyn: ",given[checktuple]-fuel)
              
            
           
    if nofuel or not listed:
        
        path = []
        print("1Ftianxw lista me tis antistoixiseis tou ",place)
        for item,key in sorted([(value,key) for (key,value) in given.items()]):
            if key[0] == place:
                placelist[key] = item
                print (key[0],key[1],item)
            elif key[1] == place:
                placelist[key[1],key[0]] = item
                print (key[1],key[0],item)
        
        for item,key in sorted([(value,key) for (key,value) in placelist.items()]):
            print("----------LOOP TURN--------")
            getin = True
            pathtemp = copy.deepcopy(pathcopy)
            for p in pathtemp[0]:
                if p[1] == key[1] or p[0] == key[1]:
                    getin = False
            if getin:
                if fuel >= item:
                    print("1Exw arketa kausima gia na paw apo to ",key[0],"sto ",key[1])
                    tempfuel = fuel
                    pathtemp[0].append(key)
                    print("1Diathesima kausima: ",fuel)
                    tempfuel -= item
                    tempfuel += available[key[1]]
                    if tempfuel>100:
                        tempfuel = 100
                    pathtemp[1] += item
                    print("1pathtemp: ",pathtemp)
                    print("1Nea diathesima kausima",tempfuel)
                    print ("1Current path: ",pathtemp[0])
                    if key[1] == 'end':
                        pathtemp.append(stop)
                        print("11Vrethike end, kanw extend to:",pathtemp)
                        path.extend(pathtemp)
                        print("11Molis ekana extend: ",path)
                        print ("TOCOPY Stop = ",stop," Pathtemp[1] = ",pathtemp[1]) 
                        if pathtemp[1]<stop:
                            print("ANATHESI STO STOP ",stop)
                            stop = pathtemp[1]
                    else:
                        print("12Kalw tin goestoend gia place = ",key[1])    
                        print ("Stop = ",stop," Pathtemp[1] = ",pathtemp[1]) 
                        if pathtemp[1]<stop:           
                            print ("Stop = ",stop," Pathtemp[1] = ",pathtemp[1]) 
                            if pathtemp[1]<stop:
                                r = dict(given)
                                if key in given.items():
                                    del r[key]
                                elif [(key[1],key[0])] in given.items():
                                    del r[(key[1],key[0])]
                                pathtemp = goestoend(available,r,tempfuel,key[1],sum,pathtemp,depth+1)
                                stop = pathtemp[2]
                                path.extend(pathtemp)
                                print(depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth)
                                print("12Molis ekana extend: ",path)
                            else:
                                print("!!!!!!!!!!!!!!!!!!!!!!!TO KOPSA!!!!!!!!!!!!!!!!!!!!!!!")
                        else:
                            print("????????????????????????????????TO KOPSA????????????????????????????????")
                else:
                    print("2Den xw arketa kausima gia na paw apo to ",key[0],"sto ",key[1])
                    print("2Kanw refuel...")
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
                        print("2mul = ",mul)
                        if mul>0:        
                            print("2Twra xw arketa kausima gia na paw apo to ",key[0],"sto ",key[1])  
                            print("2Diathesima kausima: ",fuel)               
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
                            print("2pathtemp: ",pathtemp)
                            print("2Nea diathesima kausima",tempfuel)
                            print ("2Current path: ",pathtemp[0])
                            if key[1] == 'end':
                                pathtemp.append(stop)
                                print("21Vrethike end, kanw extend to:",pathtemp)
                                path.extend(pathtemp)
                                print("21Molis ekana extend: ",path)
                                print ("TOCOPY Stop = ",stop," Pathtemp[1] = ",pathtemp[1]) 
                                if pathtemp[1]<stop:
                                    stop = pathtemp[1]
                                    print("ANATHESI STO STOP ",stop)
                            else:
                                print("22Kalw tin goestoend gia place = ",key[1])    
                                print ("Stop = ",stop," Pathtemp[1] = ",pathtemp[1]) 
                                if pathtemp[1]<stop:
                                    print ("Stop = ",stop," Pathtemp[1] = ",pathtemp[1]) 
                                    if pathtemp[1]<stop:
                                        r = dict(given)
                                        if key in given.items():
                                            del r[key]
                                        elif [(key[1],key[0])] in given.items():
                                            del r[(key[1],key[0])]
                                        pathtemp = goestoend(available,r,tempfuel,key[1],sum,pathtemp,depth+1)
                                        stop = pathtemp[2]
                                        path.extend(pathtemp)
                                        print(depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth," ",depth)
                                        print("22Molis ekana extend: ",path)
                                    else:
                                        print("!!!!!!!!!!!!!!!!!!!!!!!TO KOPSA!!!!!!!!!!!!!!!!!!!!!!!")
                                else:
                                    print("????????????????????????????????TO KOPSA????????????????????????????????")
        retpath = []
        print ("Telos LOOP")
        print("path = ")
        for x in path:
            print(x)
        mins = 10000
        for index,item in enumerate(path):
            
            if (index+2)%3 == 0:
                print("mpika gia : ")
                print(index+1," - ",item)
                if item<mins and item!=0:
                    mins = item
                    retpath = path[index - 1]
        if mins == sys.maxsize:
            mins = 0
        print("Tha kanw return to: ",retpath," , ",mins," , ",stop)
        print("------------------------------------------------------------------------------")
        return [retpath,mins,stop]

def checkfuel(available,given,fuel,place):
    path = [[],0,10000]
    path = goestoend(available,given,fuel,place,sum,path,1)
    print(path)
    if not path[0]:
        print("Can't find path")
        return "Impossible"
    else:
        print("SUCCESS! Vrethike path apo tin goestoend")
        print("Exoume sum = ",path[1])
        return str(path[1])            

t = int(input())
start_time = time.time()
for i in range(t):
    print()
    print()
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
        for item2, key2 in sorted([(value2,key2) for (key2,value2) in available.items()],reverse=True):
            print("SORTED AVAILABLE: ",item2,key2)
        for item, key in sorted([(value,key) for (key,value) in given.items()]):
            print("SORTED GIVEN: ",item,key)
        print()
        print("TERMATISE ME KAUSIMA: ",checkfuel(available,given,fuel,place))
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("KOMVOS ME APAITHSH >100")
        print("Impossible")
        