#백준 1948

import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
e=int(input())
a=[[] for _ in range(n+1)]
ra=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
result=[0]*(n+1)

for i in range(e):
    x,y,tmp=map(int,input().split())
    a[x].append((y,tmp))
    ra[y].append((x,tmp))
    indegree[y]+=1

start,end=map(int,input().split())
q=deque()
q.append(start)

while q:
    now=q.popleft()
    for i in a[now]:
        result[i[0]]=max(result[i[0]],result[now]+i[1])
        indegree[i[0]]-=1
        if indegree[i[0]]==0:
            q.append(i[0])

q.clear()
q.append(end)
count=0
visited=[False]*(n+1)
visited[end]=True

while q:
    now=q.popleft()
    for i in ra[now]:
        if result[now]==i[1]+result[i[0]]:
            count+=1
            if not visited[i[0]]:
                visited[i[0]]=True
                q.append(i[0])

print(result[end])
print(count)