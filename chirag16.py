T=int(input())
for i in range(0,T):
    N=int(input())
    A=list(map(int,input().split()))
    P=[1,2,3,4,5,6,7]
    K=0
    for j in range(0,len(A)):
        if A[j] in P:
            K=max(K,j)
        else:
            continue
    print(K+1)
