import sys
input=sys.stdin.readline

d=[[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]
mp=[[0,2,2,2,2],
    [2,1,3,4,3],
    [2,3,1,3,4],
    [2,4,3,1,3],
    [2,3,4,3,1]]

list_input=list(map(int,input().split()))
index=0
start=1
d[0][0][0]=0

while list_input[index]!=0:
    n=list_input[index]
    for i in range(5):
        if n==i:
            continue
        for j in range(5):
            d[start][i][n]=min(d[start-1][i][j]+mp[j][n],d[start][i][n])
    
    for j in range(5):
        if n==j:
            continue
        for i in range(5):
            d[start][n][j]=min(d[start-1][i][j] + mp[i][n],d[start][n][j])
    start+=1
    index+=1
start-=1
result=sys.maxsize
for i in range(5):
    for j in range(5):
        result=min(result,d[start][i][j])
print(result)