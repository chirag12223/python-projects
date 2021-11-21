import math
T=int(input())
for i in range(0,T):
    a,b,A,B=map(int,input().split())
    print(math.ceil(A/a)+math.ceil(B/b))