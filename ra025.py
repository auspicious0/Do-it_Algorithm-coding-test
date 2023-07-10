#백준 온라인 저지 13023번
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m=map(int,input().split())
visited=[False]*n
edge=[[] for i in range(n)]
arrive=False

def DFS(k,cnt):
    global arrive
    if cnt==5:
        arrive=True
        return
    visited[k]=True
    for i in edge[k]:
        if visited[i]==False:
            DFS(i,cnt+1)
    visited[k]=False

for i in range(m):
    x,y=map(int,input().split())
    edge[x].append(y)
    edge[y].append(x)

for i in range(n):
    DFS(i,1)
    if arrive:
        print(1)
        break
else:
    print(0)