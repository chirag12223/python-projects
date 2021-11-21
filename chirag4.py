nums=list(map(int,input().split()))
c=0
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if i==j:
            continue
        else:
            if nums[i]>nums[j]:
                c+=1
print(c)