nums=list(map(int,input().split()))
k=int(input())
nums.sort()
t=10**9+1
nums.reverse()
if k==1:
    print(0)
else :
    i=0
    while i+k<=len(nums):
        B=list(nums[i:i+k])
        t=min(t,B[0]-B[len(B)-1])

        i+=1
    print(t)