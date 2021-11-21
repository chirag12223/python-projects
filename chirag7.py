matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target =13
for i in range(0,len(matrix)-1):
            if matrix[i][0]<=target and matrix[i+1][0]>target:
                k=i
                print(k)
                if target in matrix[i]:
                    print("A")
                    print("true")
                    exit()
                else:
                    print("false")
                    exit()
if target in matrix[len(matrix)-1]:
      print("true")
else:
    print("false")
