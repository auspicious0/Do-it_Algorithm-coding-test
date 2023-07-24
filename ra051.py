import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n=int(input())
parent=[i for i in range(n+1)]
m=int(input())

def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

def check(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return True
    else:
        return False

for i in range(n):
    num=list(map(int,input().split()))
    for j in range(n):
        if num[j]==1:
            union(i+1,j+1)

final=list(map(int,input().split()))

for i in range(m-1):
    x,y=final[i],final[i+1]
    if check(x,y)==False:
        print('NO')
        break
else:
    print('YES')