import math
nums=list(map(int,input().split()))
c=[]
C=0
t=-1*(10**5)
K=nums[0]
for i in range(0,len(nums)):
    for j in range (i,len(nums)):

        if i==j:
            continue
        else:
            c.append(list(nums[i:j+1]))
for i in range(0,len(c)):
    for j in range(0,len(c[i])):
        print(1)
        C+=c[i][j]
    if C>t:
        t=C
    C=0

print(t,C)
for i in range(0,len(nums)):
    if nums[i]>=t:
        t=nums[i]
print(t)