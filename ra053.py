from collections import deque

node,edge=map(int,input().split())
a=[[] for _ in range(node+1)]
indegree=[0]*(node+1)

for i in range(edge):
    start,end=map(int,input().split())
    a[start].append(end)
    indegree[end]+=1

q=deque()
for i in range(1,node+1):
    if indegree[i]==0:
        q.append(i)

while q:
    now=q.popleft()
    print(now,end=' ')
    for end in a[now]:
        indegree[end]-=1
        if indegree[end]==0:
            q.append(end)
