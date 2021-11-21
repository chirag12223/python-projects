T=int(input())
for i in range(0,T):
    A=input()
    K=list(A[2:len(A)])
    E=""
    S=[]
    print(K)
    print(K)
    for t in range(0,len(K)):
        if K[t]==" " or t==len(K)-1:
            S.append(E)
            E=""
        else:
            E+=K[t]

        if K[len(K)-2]!=" ":
            S[len(S)-1].append(K[len(K)-1])
        else:
            S.append(K[len(K)-1])
    print(S)