nums=list(map(int,input().split()))
min=(10**4)+1
max=0
for i in range(0,len(nums)-1):
    if nums[i]<min:
        k=i
        min=nums[i]
    if nums[i+1]-nums[k]>max:
        max=nums[i]-nums[k]
print(max)