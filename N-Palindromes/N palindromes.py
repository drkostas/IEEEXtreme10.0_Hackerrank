def check(count,name,n):
    print(len(name),n,name)
    ispal = True
    for i in range(len(name)):
        if name != name[::-1]:
            ispal=False
    if ispal:
        count+=1
        print("ok")
        
        
t = int(input())
for i in range(t):    
    count = 0
    name = []
    n,name2 =  [x for x in input().split()]
    name = list(name2)
    n = int(n)
    print(check(count,name,n))
        