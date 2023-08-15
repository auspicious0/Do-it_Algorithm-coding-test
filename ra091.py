import sys
input=sys.stdin.readline
n,m=map(int,input().split())
rec=[0 for i in range(n)]
max=0

for i in range(n):
    rec[i]=list(map(int,input().rstrip()))
    for j in range(m):
        if rec[i][j]==1 and i>0 and j>0:
            rec[i][j]=min(rec[i-1][j-1],rec[i-1][j],rec[i][j-1])+rec[i][j]
        if rec[i][j]> max:
            max=rec[i][j]
print(int(max**2))