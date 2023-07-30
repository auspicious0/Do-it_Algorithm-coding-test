import sys
input=sys.stdin.readline
n,m=map(int,input().split())
floid=[[sys.maxsize]*(n+1) for i in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    floid[x][y]=1
    floid[y][x]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            floid[i][j]=min(floid[i][j],floid[i][k]+floid[k][j])

target=sum(floid[1])
result=1
for i in range(2,n+1):
    if target>sum(floid[i]):
        result=i
        target=sum(floid[i])

print(result)