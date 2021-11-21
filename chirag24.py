import math
T=int(input())
for i in range (0,T):
    A,B=map(int,input().split())
    C=(A+B)//2
    print(math.ceil((B-C)/2)+math.ceil((C-A)/2))