T=int(input())
for J in range(0,T):
    A,B,X,Y=map(int,input().split())
    c=1
    k=1
    C=1
    K=1
    d=[]
    e=[]
    D=[]
    E=[]
    for i in range(0,A-1):
        c+=2+i
    for i in range(0,B-1):
        k+=1+i
    for i in range(0,B):
        d.append(c)
        c+=A+i
    for i in range(0,A):
        k+=B+i+1
    print(d,D)
    for i in range(0,X-1):
        C+=2+i
    for i in range(0,Y-1):
        K+=i
    for i in range(0,Y):
        D.append(C)
        C+=X+i
    for i in range(0,X):
        K+=Y+i+1
    j=1
    for i in range(0,A):
        e.append(j)
        j+=2+i
    W = 1
    for i in range(0, X):
        E.append(W)
        W += 2 + i
    print(e,E,d,D)
    p=0
    q=0
    P=0
    Q=0
    for i in range(1,len(d)):
        p+=d[i]
    for i in range(0,len(e)):
        q+=e[i]
    for i in range(1,len(D)):
        P+=D[i]
    for i in range(0,len(E)):
        Q+=E[i]

    print(Q+P-p-q)