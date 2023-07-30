#백준 1219번 문항
import sys
input=sys.stdin.readline
n,s,e,edge=map(int,input().split())
result=[-sys.maxsize]*(n)
edges=[]

for i in range(edge):
    x,y,tmp=map(int,input().split())
    edges.append((x,y,tmp))

money=list(map(int,input().split()))
result[s]=money[s]

for i in range(n+101):
    for x,y,tmp in edges:
        if result[x]==-sys.maxsize:
            continue
        elif result[x]==sys.maxsize:
            result[y]=sys.maxsize
        else:
            if result[y]<result[x]+money[y]-tmp:
                result[y]=result[x]+money[y]-tmp
                if i>=n-1:
                    result[x],result[y]=sys.maxsize,sys.maxsize

if result[e]==-sys.maxsize:
    print("gg")
elif result[e]==sys.maxsize:
    print("Gee")
else:
    print(result[e])