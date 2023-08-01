from collections import deque
from queue import PriorityQueue
import copy
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
land=[0 for i in range(n)]
visited=[[False for i in range(m)] for i in range(n)]
x=[0,1,0,-1]
y=[1,0,-1,0]

for i in range(n):
    land[i]=list(map(int,input().split()))

sNum=1
result_land=list([])
now_land=[]

def appendNode(i,j,queue):
    land[i][j]=sNum
    visited[i][j]=True
    tmp=[i,j]
    now_land.append(tmp)
    queue.append(tmp)

def bfs(i,j):
    q=deque()
    now_land.clear()
    start=[i,j]
    land[i][j]=sNum
    now_land.append(start)
    q.append(start)
    visited[i][j]=True
    land[i][j]=sNum
    while q:
        r,c=q.popleft()
        for k in range(4):
            dx=x[k]
            dy=y[k]

            while 0<=dx+r<n and 0<=dy+c<m:
                if not visited[dx+r][dy+c] and land[dx+r][dy+c]!=0:
                    appendNode(dx+r,dy+c,q)
                else:
                    break
                if dx<0:
                    dx-=1
                elif dx>0:
                    dx+=1
                elif dy<0:
                    dy-=1
                elif dy>0:
                    dy+=1
    return now_land

for i in range(n):
    for j in range(m):
        if land[i][j]!=0 and not visited[i][j]:
            tmp_list=copy.deepcopy(bfs(i,j)) 
            result_land.append(tmp_list)
            sNum+=1
pq=PriorityQueue()
for next in result_land:
    for now in next:
        r=now[0]
        c=now[1]
        check=land[r][c]
        for i in range(4):
            dx=x[i]
            dy=y[i]
            length=0
            while 0<=r+dx<n and 0<=c+dy<m:
                if check==land[r+dx][c+dy]:
                    break
                elif land[r+dx][c+dy]!=0:
                    if length>1:
                        pq.put((length,check,land[r+dx][c+dy]))
                    break
                elif land[r+dx][c+dy]==0:
                    length+=1
                if dx>0:
                    dx+=1
                elif dx<0:
                    dx-=1
                elif dy>0:
                    dy+=1
                elif dy<0:
                    dy-=1

parent=[i for i in range(sNum)]
def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a
result=0
edges=0
while pq.qsize()>0:
    tmp,q,w=pq.get()
    if find(q)!=find(w):
        union(q,w)
        result+=tmp
        edges+=1
if edges==sNum-2:
    print(result)
else:
    print(-1)