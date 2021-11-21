N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=[]
for i in range(0,Q):
    S=int(input())
    B.append(S)
A.sort()
k=len(A)-1
for i in range(0,len(B)):


