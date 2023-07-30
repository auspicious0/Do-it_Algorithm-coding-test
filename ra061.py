import sys
input=sys.stdin.readline
n=int(input())
e=int(input())
floid=[[sys.maxsize]*(n+1) for i in range(n+1)]

for i in range(e):
    x,y,tmp=map(int,input().split())
    floid[x][y]=min(floid[x][y],tmp)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                floid[i][j]=0
            else:
                floid[i][j]=min(floid[i][j],floid[i][k]+floid[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if floid[i][j]==sys.maxsize:
            print(0,end=' ')
        else:
            print(floid[i][j],end=' ')
    print()