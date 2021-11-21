T=int(input())
for i in range(0,T):
    a,b=map(int,input().split())
    N=list(map(int,input().split()))
    M=list(map(int,input().split()))
    for j in range(0,len(M)):
        k=M[j]-1
        if N[k]==1 or N[k]==2:
            print(0,end=" ")
        else:
            J=list(N[0:k])
            q=len(J)-1
            s=k
            while q>=0:
                if J[q]==1:
                    s=k-q
                    break
                q-=1
            Z=list(N[k+1:len(N)])
            p=k
            print(Z,N)
            for q in range(0,len(Z)):
                if Z[q]==2 :
                    p = q+1
                    break
            if s!=p or s!=q:
                print(min(s,p),end=" ")
            else:
                print(-1,end=" ")
        print()