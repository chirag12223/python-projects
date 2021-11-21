T=int(input())
for i in range(0,T):
    D={}
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    for j in range(0,len(A)):
        if A[j]in D:
            D[A[j]]+=1
        else:
            D[A[j]]=1
    Z=[]
    W=list(D.keys())
    P=W[::-1]
    F=list(D.values())
    for j in range(0,len(F)):
        if F[j]==2:
            Z.append(j)
        elif F[j]>2:
            print(-1)
            print()
            break
    if len(Z)==0:
        for j in range(0, len(W)):
            print(P[j],end=" ")
        print()
    elif len(Z)>1:
        print(-1)
        print()
    else:
        if Z[0]==len(Z)-1:
            print(-1)
            print()
        else :
            b=W[Z[0]]
            W.append(b)
            for j in range(0, len(W)):
                print(P[j], end=" ")
            print()