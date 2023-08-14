import sys
input=sys.stdin.readline
mod=10007
n,k=map(int,input().split())
d=[[0 for j in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    d[i][0]=1
    d[i][i]=1
    d[i][1]=i
for i in range(3,n+1):
    for j in range(2,i):
        d[i][j]=(d[i-1][j]+d[i-1][j-1])%mod
print(d[n][k])