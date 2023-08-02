import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
p=list(map(int,input().split()))
visited=[False]*(n)
tree=[[] for _ in range(n)]
answer=0
root=0
deleteNode=int(input())

for i in range(n):
    if p[i]==-1:
        root=i
    else:
        tree[p[i]].append(i)
        tree[i].append(p[i])

def dfs(number):
    global answer
    cNode=0
    visited[number]=True
    for i in tree[number]:
        if not visited[i] and i!=deleteNode:
            cNode+=1
            dfs(i)
    if cNode==0:
        answer+=1
if root==deleteNode:
    print(0)
else:
    dfs(root)   
    print(answer)