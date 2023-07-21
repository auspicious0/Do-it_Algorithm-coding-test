#백준 온라인 저지 18352
from collections import deque
import sys
input=sys.stdin.readline

n,m,k,x=map(int,input().split())
a=[[] for _ in range(n+1)]
for i in range(m):
    num1,num2=map(int,input().split())
    a[num1].append(num2)
visited=[-1]*(n+1)

def bfs(v):
    q=deque()
    q.append(v)
    visited[v]+=1
    while q:
        now=q.popleft()
        for i in a[now]:
            if visited[i]==-1:
                visited[i]=visited[now]+1
                q.append(i)
bfs(x)
answer=[]
for i,v in enumerate(visited):
    if v==k:
        answer.append(i)

if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)