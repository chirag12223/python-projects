T=int(input())
for i in range(0,T):
    N,A,B,C=map(int,input().split())
    k=max(min(A,B)+min(B,C))
    if min(A,B)>min(B,C):
        k+=min(B-k,C)
    else:
        k+=min(A,B-k)
    if k>N:
        print("YES")
    else:
        print("NO")