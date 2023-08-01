#백준 온라인 저지 1414번

from queue import PriorityQueue
n=int(input())
pq=PriorityQueue()
parent=[i for i in range(n+1)]
sentence='0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalsize=0

for i in range(n):
    alpha=list(map(str,input()))
    for j in range(n):
        if alpha[j]=='0':
            continue
        tmp=sentence.index(alpha[j])
        totalsize+=tmp
        pq.put((tmp,i,j))

def find(x):
    if x==parent[x]:
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
while pq.qsize()>0:
    tmp,x,y=pq.get()
    if find(x)!=find(y):
        union(x,y)
        edges+=1
        result+=tmp
if edges==n-1:
    print(totalsize-result)
else:
    print(-1)