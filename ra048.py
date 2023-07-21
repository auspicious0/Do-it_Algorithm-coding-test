#백준 온라인 저지 1707
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
check=[]
visited=[False]
a=[[]]
checkeven=True

def dfs(v):
    global checkeven
    visited[v]=True
    for i in a[v]:
        if visited[i]==False:
            check[i]=(check[v]+1)%2
            dfs(i)
        elif check[i]==check[v]:
            checkeven=False
            return

for i in range(n):
    v,e=map(int,input().split())
    a=[[] for _ in range(v+1)]
    visited=[False]*(v+1)
    check=[0]*(v+1)

    for j in range(e):
        num1,num2=map(int,input().split())
        a[num1].append(num2)
        a[num2].append(num1)
    
    for j in range(1,v+1):
        if checkeven:
            dfs(j)
        else:
            print('NO')
            break
    else:
        print('YES')
    checkeven=True