# cook your dish here
T = int(input())
for i in range(0, T):
    N = int(input())
    A = list(map(int, input().split()))
    c = 0
    d = 0
    B = []
    C = []
    for j in range(0, len(A)):
        if A[j] % 2 == 1:
            B.append(A[j])
            c += 1
        else:
            C.append(A[j])
            d+=1
    if c==0 or d==0:
        print(-1)
    else:
        D = C + B

        for k in range(0, len(D)):
            print(D[k], end=" ")
    print()