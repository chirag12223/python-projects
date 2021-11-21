T=int(input())
for i in range (0,T):
    N=int(input())
    A=list(map(int,input().split()))
    C=[]
    for j in range(0,len(A)):
        B=[]
        for k in range(j,len(A)):
            B.append(A[k])
            print(B)
            C.append(B)
            print(B,C)
        print(C)
    print(C)


