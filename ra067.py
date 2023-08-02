import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
visited=[False]*(n+1)
answer=[0]*(n+1)
tree=[[] for _ in range(n+1)]

for i in range(n-1):
    x,y=map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

def dfs(number):
    visited[number]=True
    for i in tree[number]:
        if visited[i]==False:
            answer[i]=number
            dfs(i)
dfs(1)
for i in range(2,len(answer)):
    print(answer[i])