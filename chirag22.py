def findpower(base, power):
    mod = 10 ** 9 + 7
    res = 1
    while power != 0:
        if power % 2 == 0:
            base = ((base % mod) * (base % mod)) % mod
            power = power // 2
        elif power%2==1:
            res = ((res % mod) * (base % mod)) % mod
            power = power - 1
            return res
T=int(input())
u=(10**9)+7
for  z in range(0,T):
    L,R=map(int,input().split())
    D=[]
    for  k in range(L,R+1):
        A = str(k)
        B = A[0:len(A) - 1]
        B = B[::-1]
        D.append(A+B)
    W=0
    L=D[0]
    for t in range(1,len(D)):
        W+=int(D[t])
    print(findpower(L,W))