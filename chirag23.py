import math
T =int(input())
for i in range(0,T):
    E,K=map(int,input().split())

    c=0


    while math.floor(E/K)!=0:
        E=math.floor(E/K)
        c+=1
    print(c+1)