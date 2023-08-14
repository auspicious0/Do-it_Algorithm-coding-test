#백준 11437 
import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write
n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
depth=[0]*(n+1)
parent=[0]*(n+1)
visited=[False]*(n+1)

def bfs(k):
    visited[k]=True
    length=1
    now_level=1
    count=0
    q=deque()
    q.append(k)
    while q:
        p=q.popleft()
        for i in tree[p]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
                parent[i]=p
                depth[i]=length
        count+=1
        if now_level==count:
            length+=1
            count=0
            now_level=len(q)
bfs(1)

def execute(a,b):
    if depth[a]<depth[b]:
        a,b=b,a
    while depth[a]!=depth[b]:
        a=parent[a]
    while a!=b:
        a=parent[a]
        b=parent[b]
    return a
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    print(str(execute(a,b)))
    print("\n")