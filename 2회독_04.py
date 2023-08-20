import sys
input=sys.stdin.readline
n,m=map(int,input().split())
maps=[0 for i in range(n+1)]
for i in range(1,n+1):
    maps[i]=list(map(int,input().split()))
    maps[i].insert(0,0)
smaps=[[0 for j in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        smaps[i][j]=maps[i][j]+smaps[i-1][j]+smaps[i][j-1]-smaps[i-1][j-1]
for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(smaps[x2][y2]-smaps[x1-1][y2]-smaps[x2][y1-1]+smaps[x1-1][y1-1])