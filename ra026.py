#백준 온라인 저지 1260

import sys
from collections import deque
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m,s=map(int,input().split())
visited=[False]*(n+1)
edge=[[] for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    edge[x].append(y)
    edge[y].append(x)

for i in range(1,n+1):
    edge[i].sort()
def DFS(k):
    visited[k]=True
    print(k,end=" ")
    for i in edge[k]:
        if visited[i]==False:
            DFS(i)

DFS(s)

def BFS(k):
    q=deque()
    q.append(k)
    visited[k]=True
    while q:
        tmp=q.popleft()
        print(tmp,end=" ")
        for i in edge[tmp]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)

print()

visited=[False]*(n+1)
BFS(s)
