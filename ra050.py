import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n,m=map(int,input().split())
parent=[i for i in range(n+1)]

def find(a):
    if parent[a]==a:
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

for i in range(m):
    checker,a,b=map(int,input().split())
    if checker==0:
        union(a,b)
    else:
        if check(a,b):
            print("YES")
        else:
            print("NO")
