T=int(input())
for i in range(0,T):
    a,b,c,d,K=map(int,input().split())
    if abs(c-a)+abs(b-d)==K:
        print("YEs")
    elif abs(c-a)+abs(b-d)>K and (K-abs(c-a)+abs(b-d)):
        print("YES")
    else:
        print("NO")