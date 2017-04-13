import re

t = int(input())
x = []
first = []
second = []
question = []
sep = []
answer = []
q = []
n = []

x2 = []
first2 = []
second2 = []
question2 = []
sep2 = []
answer2 = []

x3 = []
first3 = []
second3 = []
question3 = []
for i in range(t):
    _ = input()
    q2,n2 = [int(x) for x in input().split()]
    q.append(q2)
    n.append(n2)
    for j in range(q2):
        for k in re.split("( and | or |[^a-zA-Z0-9 ]+)",input()):
            x3.append(k)
           
        for y in x3:
            if y==" and " or y==" or ":
                sep2.append(y[1:-1])
            else:
                sep2.append('')
                
        x3 = [y for y in x3 if y != " and " and y !=" or " ]
        
        for k in x3:
            qu, fr, sc = [k for k in k.split()]
            question3.append(qu)
            first3.append(fr)
            second3.append(sc)
            
        answer2 = input()
        x2.append(x3)
        first2.append(first3)
        second2.append(second3)
        question2.append(question3)
        x3=[]
        first3=[]
        second3=[]
        question3=[]
    answer.append(answer2)   
    x.append(x2)
    first.append(first2)
    second.append(second2)
    question.append(question2)
    sep.append(sep2)
    answer.append(answer2)
    x2=[]
    first2=[]
    second2=[]
    question2=[]
    sep2=[]
    q2=[]
    answer2=[]
print("q: ",q,"n: ",n,"x:",x,"first: ",first,"second: ",second,"question: ",question,"sep: ", sep,"answer: ",answer)   

flscount=0
for i in range(t):#in testcase
    
    for j in range(q[i]):#in sentence
        truth = True
        balloonstemp = ['rgb','rgb','rgb','rgb','rgb','rgb','rgb','rgb','rgb','rgb'] 
        #anazitisi lathous
        if q[i] == n[i]:
            print("mpika")
            truth = False
            for k in range(len(question[i][j])):#in individual expression 
                if (answer[i][j] == 'no'):
                    if sep[i][j]=='and':
                        sep[i][j] = 'or'
                    elif sep[i][j]=='or':
                        sep[i][j]= 'and'
        elif n[i] != 0:
            print("mpika2")
            count = 0
            for k in range(len(question[i][j])):#in individual expression            
                if question[i][j][k]=='count':               
                    print("mpika3")
                    if (answer[i][j] == 'yes'):
                        print("mpika4")
                        if (sep[i][j]=='and' or sep[i][j]==''):
                           count+=int(second[i][j][k])
                    elif not(sep[i][j]=='and' or sep[i][j]==''):
                        count+=int(second[i][j][k])
            print(count)          
            if count>=10:
                truth = False
                for k in range(len(question[i][j])):#in individual expression 
                    if sep[i][j]=='and':
                        sep[i][j] = 'or'
                    elif sep[i][j]=='or':
                        sep[i][j]='and'
                
        #dimiourgia balloon gia and kai gia or  
        for k in range(len(question[i][j])):#in individual expression            
            if question[i][j][k]=='color':               
                if (answer[i][j] == 'yes' and truth) or (answer[i][j] == 'no' and not truth):
                    if sep[i][j][k]=='and' or sep[i][j]=='':
                        balloonstemp[int(first[i][j][k])-1] = second[i][j][k]
                else:
                    if sep[i][j]=='and' or sep[i][j]=='':
                        balloonstemp[int(first[i][j][k])-1] = "rgb".replace(second[i][j][k], '')
                
        for k in range(len(question[i][j])):#in individual expression            
            if question[i][j][k]=='color':               
                if (answer[i][j] == 'yes' and truth) or (answer[i][j] == 'no' and not truth):
                    if sep[i][j]=='or' :
                        if balloonstemp[int(first[i][j][k])-1] == 'rgb':
                            balloonstemp[int(first[i][j][k])-1] = second[i][j][k]
                else:
                    if sep[i][j]=='or' :
                        if balloonstemp[int(first[i][j][k])-1] == 'rgb':
                            balloonstemp[int(first[i][j][k])-1] = "rgb".replace(second[i][j][k], '')
        
        
    print(" ".join(balloonstemp))