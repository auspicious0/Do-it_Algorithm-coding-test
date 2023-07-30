import sys
input=sys.stdin.readline
n,e=map(int,input().split())
edges=[]
distance=[sys.maxsize]*(n+1)

for i in range(e):
    x,y,tmp=map(int,input().split())
    edges.append((x,y,tmp))

distance[1]=0

for i in range(n-1):
    for x,y,tmp in edges:
        if distance[x]!=sys.maxsize and distance[y]>distance[x]+tmp:
            distance[y]=distance[x]+tmp

cicle=False

for x,y,tmp in edges:
    if distance[x]!=sys.maxsize and distance[y]>distance[x]+tmp:
        cicle=True
        break
if cicle:
    print(-1)
else:
    for i in range(2,len(distance)):
        if distance[i]==sys.maxsize:
            print(-1)
        else:
            print(distance[i])