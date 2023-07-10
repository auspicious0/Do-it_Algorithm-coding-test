from collections import deque
n=int(input())
a=[[] for i in range(n+1)]

for i in range(n):
    input_value=list(map(int,input().split()))
    index=0
    start=input_value[index]
    while True:
        if input_value[index+1]==-1:
            break
        a[start].append((input_value[index+1],input_value[index+2]))
        index+=2

record=[0]*(n+1)
visited=[False]*(n+1)

def bfs(k):
    q=deque()
    q.append(k)
    visited[k]=True
    while q:
        now_node=q.popleft()
        for end_value in a[now_node]:
            if visited[end_value[0]]==False:
                visited[end_value[0]]=True
                q.append(end_value[0])
                record[end_value[0]]=record[now_node]+end_value[1]

bfs(1)
MAX=1
for i in range(2,n+1):
    if record[MAX] <record[i]:
        MAX=i

record=[0]*(n+1)
visited=[False]*(n+1)      
bfs(MAX)
print(max(record)) 