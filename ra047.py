# 백준 온라인 저지 1325번
import sys
from collections import deque
input=sys.stdin.readline
n,e=map(int,input().split())
a=[[] for _ in range(n+1)]
answer=[0]*(n+1)
visited=[False]*(n+1)

for i in range(e):
    x,y=map(int,input().split())
    a[x].append(y)

def bfs(v):
    q=deque()
    q.append(v)
    visited[v]=True
    while q:
        now=q.popleft()
        for i in a[now]:
            if visited[i]==False:
                visited[i]=True
                answer[i]+=1
                q.append(i)

for i in range(1,n+1):
    visited=[False]*(n+1)
    bfs(i)

max_value=max(answer)
for i,v in enumerate(answer):
    if v==max_value:
        print(i,end=" ")