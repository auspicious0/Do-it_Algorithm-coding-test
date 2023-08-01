from queue import PriorityQueue

n,e=map(int,input().split())
parent=[i for i in range(n+1)]
pq=PriorityQueue()

for i in range(e):
    x,y,tmp=map(int,input().split())
    pq.put((tmp,x,y))

def find(x):
    if parent[x]==x:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

edges=0
result=0
while edges<n-1:
    tmp,x,y=pq.get()
    if find(x)!=find(y):
        union(x,y)
        result+=tmp
        edges+=1
print(result)