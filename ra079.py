import sys
input=sys.stdin.readline
t=int(input())
d=[[0 for j in range(30)] for i in range(30)]
for i in range(30):
    d[i][1]=i
    d[i][i]=1
    d[i][0]=1
for i in range(3,30):
    for j in range(2,i):
        d[i][j]=d[i-1][j]+d[i-1][j-1]
for i in range(t):
    a,b=map(int,input().split())
    print(d[b][a])