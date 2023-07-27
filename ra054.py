from collections import deque

n=int(input())
indegree=[0]*(n+1)
a=[[] for _ in range(n+1)]
result=[0]*(n+1)
timechecker=[0]*(n+1)

for i in range(1,n+1):
    buildlist=list(map(int,input().split()))
    del buildlist[-1]
    timechecker[i]=buildlist[0]
    for j in range(1,len(buildlist)):
        a[buildlist[j]].append(i)
        indegree[i]+=1

q=deque()

for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    now=q.popleft()
    for i in a[now]:
        result[i]=max(result[i],result[now]+timechecker[now])
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)

for i in range(1,n+1):
    print(timechecker[i]+result[i])