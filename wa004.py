#wrong answer #구간합 이용을 적절히 하지 못함.
n,m=map(int,input().split())
numbers=[[0]]#계산을 평이하게 하기 위함
for i in range(n):
    numbers.append(list(map(int,input().split())))
temp=0
for i in range(1,n+1):#index out of range 
    for j in range(n):
        temp+=numbers[i][j]
        numbers[i][j]=temp
for i in range(m):
    result=0
    x1,y1,x2,y2=map(int,input().split())
    result=numbers[x2][y2-1]
    for j in range(x1,x2+1):
        result-=(numbers[j][y1-2]-numbers[j][y1-3])
    print(result)
