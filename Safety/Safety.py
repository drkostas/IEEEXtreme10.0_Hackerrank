p = input()
password = []
current = []
password =list(p)
current = password[:]
numoftests = int(input())
for i in range(numoftests):
    tests = [int(x) for x in input().split()]
    if tests[0] == 1 :
        if current[tests[1]-1:tests[2]] == current[tests[3]-1:tests[2]-tests[1]+tests[3]]:
            print("Y")
        else:
            print("N")
    elif tests[0] == 2:
        current[tests[1]-1:tests[2]] = password[tests[3]-1:tests[2]-tests[1]+tests[3]]
    elif tests[0] ==3:
        for count in range(tests[1],tests[2]):
            if ord(current[count])!=122:
                current[count] = chr(ord(current[count]) + 1)
            else:
                current[count] =  'a'
            