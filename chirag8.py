# cook your dish here
# cook your dish here
T=int(input())
for i in range(0,T):
    N,M,K=map(int,input().split())
    L=list(map(int,input().split()))
    D={}
    for j in range(0,len(L)):
        if L[j]in D:
            D[L[j]]+=1
        else:
            D[L[j]]=1
    c=0
    Q=[]
    for a in D:
        if a<=N and D[a]>1:
            c+=1
            Q.append(a)
    print(c,end=" ")
    for o in range(0,len(Q)):
        print(Q[o],end=" ")
    print()