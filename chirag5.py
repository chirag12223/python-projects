nums=list(map(int,input().split()))
max=0
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if i==j:
            continue
        else:
            k=-1*(nums[i]-nums[j])
            if k>max:
                max=k

print(max)