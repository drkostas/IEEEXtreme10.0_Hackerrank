T = int(input())

for j in range(T):
    N = int(input())
    petal = -1
    for i in range(N):
        petal += 2
        if petal == i:
            petal = -1
    print(petal)