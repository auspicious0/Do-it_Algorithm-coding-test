#백준 온라인 져지 11724
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m=map(int,input().split())
a=[[] for _ in range(n+1)]
visited=[False]*(n+1)

def DFS(k):
    visited[k]=True
    for i in a[k]:
        if visited[i] ==False:
            DFS(i)

for _ in range(m):
    x,y=map(int,input().split())
    a[x].append(y)
    a[y].append(x)

count=0
for i in range(1,n+1):
    if visited[i]==False:
        count+=1
        DFS(i)
print(count)