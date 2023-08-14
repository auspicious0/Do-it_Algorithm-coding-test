#백준 11438
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
visited=[False]*(n+1)
temp=1
kmax=0

while temp<=n:
    temp*=2
    kmax+=1

parent=[[0 for j in range(n+1)] for _ in range(kmax+1)]

def bfs(node):
    q=deque()
    q.append(node)
    visited[node]=True
    length=1
    level=1
    count=0
    while q:
        now_node=q.popleft()
        for i in tree[now_node]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
                parent[0][i]=now_node
                depth[i]=length
        count+=1
        if count==level:
            count=0
            level=len(q)
            length+=1
bfs(1)

for i in range(1,kmax+1):
    for j in range(1,n+1):
        parent[i][j]=parent[i-1][parent[i-1][j]]

def executeLCA(a,b):
    if depth[a]>depth[b]:
        a,b=b,a
    for k in range(kmax,-1,-1):
        if pow(2,k)<=depth[b]-depth[a]:
            b=parent[k][b]
    for k in range(kmax,-1,-1):
        if a==b:
            break
        if parent[k][a] != parent[k][b]:
            a=parent[k][a]
            b=parent[k][b]
    if a!=b:
        return parent[0][a]
    else:
        return a
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    print(str(executeLCA(a,b)))
    print('\n')