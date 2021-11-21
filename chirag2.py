numRows=int(input())
k=1
K=[]
arr=[]
def fact(n):
    k=1
    if n==0:
        return 1
    for i in range(1,n+1):
        k*=i
    return k
for i in range(0,numRows):
    arr=[]
    for j  in range(0,i+1):
        arr.append(fact(i)//(fact(j)*fact(i-j)))

    K.append(arr)
print(K)