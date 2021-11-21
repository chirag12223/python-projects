T=int(input())
for i in range(0,T):
    N,K=map(int,input().split())
    A=list(input())
    B=list(map(int,input().split()))
    c=0
    for z in range(0,len(A)-1):
        if A[z]==A[z+1]:
            c+=2
        else:
            c+=1
    for j in range(0,len(B)):
        B[j]=B[j]-1
    for j in range(0, len(B)):
        if A[B[j]] =="0":
            A[B[j]] ="1"

        elif A[B[j]] =="1":
            A[B[j]]="0"
        if B[j]==0:
            if A[B[j]]!=A[B[j+1]]:
                c-=1
        elif B[j]==len(A)-1:

