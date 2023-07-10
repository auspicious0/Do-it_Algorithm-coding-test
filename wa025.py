#백준 온라인 저지 13023번
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
n,m=map(int,input().split())
visited=[False]*(n)
line=[[] for i in range(n)]
count=0

def DFS(k):
    global count
    count+=1
    if count==4:
        count=0
        return True
    visited[k]=True
    for i in line[k]:
        if visited[i]==False:
            DFS(i)
    visited[k]=False
for i in range(m):
    x,y=map(int,input().split())
    line[x].append(y)
    line[y].append(x)

for i in range(n):
    if DFS(i)==True:
            print(1)
            break
else:
    print(0)