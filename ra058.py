import sys
import heapq
input=sys.stdin.readline

n,e,k=map(int,input().split())
a=[[] for _ in range(n+1)]
result=[[sys.maxsize]*k for _ in range(n+1)]

for i in range(e):
    x,y,tmp=map(int,input().split())
    a[x].append((y,tmp))
q=[[0,1]]
result[1][0]=0

while q:
    tmp,target=heapq.heappop(q)
    for next,temp in a[target]:
        if temp+tmp<result[next][k-1]:
            result[next].append(temp+tmp)
            heapq.heappush(q,[temp+tmp,next])
            result[next].sort()
for i in range(1,n+1):
    if result[i][k-1]==sys.maxsize:
        print(-1)
    else:
        print(result[i][k-1])