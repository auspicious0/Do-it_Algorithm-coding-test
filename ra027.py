#백준 온라인 저지 2178
from collections import deque
n,m=map(int,input().split())
vertex=[]
visited=[[False]*m for i in range(n)]
move=[(1,0),(0,1),(-1,0),(0,-1)]
for i in range(n):
    x=list(map(int,input()))
    vertex.append(x)

def BFS():
    q=deque([(0,0)])#deque([(,)])
    visited[0][0]=True
    while q:
        x,y=q.popleft()
        for i in move:
            dx=x+i[0]
            dy=y+i[1]
            if 0<=dx<n and 0<=dy<m and vertex[dx][dy]!=0 and visited[dx][dy]==False:
                vertex[dx][dy]=vertex[x][y]+1
                visited[dx][dy]=True
                q.append((dx,dy))
BFS()
print(vertex[n-1][m-1])