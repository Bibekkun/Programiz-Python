a=[[1,2],
  [2,3],
  [3,4]]
b=[[4,5],
  [5,6],
  [6,7]]
result=[[0,0],
       [0,0],
       [0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j]=a[i][j]+b[i][j]
for r in result:
    print(r)