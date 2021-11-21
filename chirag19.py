import math
T=int(input())
for i in range(0,T):
    N=int(input())
    A=list(map(int,input().split()))
    B=[0,A[0]]
    k=A[0]
    for j in range(1,len(A)-1):
        B.append(math.gcd(A[j],k))
        k=math.gcd(k,A[j])
    print(B)
    (A.reverse())
    D = [0, A[0]]
    k =A[0]
    for j in range(1, len(A) - 1):
        D.append(math.gcd(A[j], k))
        k = math.gcd(k, A[j])
    D.reverse()
    print(D)
    mid=[]
    mid.append(D[0])
    for  p in range(1,len(D)-1):
        mid.append(math.gcd(B[p],D[p]))
    mid.append(B[len(B)-1])
    print(mid)
    K=max(mid)
    I=[]
    X=[]
    for l in range(0,len(mid)):
        if mid[l]==K:
          I.append(l)
    for e in range(0,len(I)):
        X.append(A[I[e]])
    print(I)
    print(A[I[0]])
    E=max(X)
    print(E)
    print(X)
    A.remove(E)
    A.append(K)
    O=0
    for G in range(0,len(A)):
        O+=A[G]
    print(O//K)