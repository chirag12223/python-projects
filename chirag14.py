# cook your dish here
K=10**9+7
T=int(input())
for i in range(0,T):
    N,M =map(int,input().split())
    print(((2**N-1)**M)%K)