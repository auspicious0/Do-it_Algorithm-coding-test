from queue import PriorityQueue
import sys
input=sys.stdin.readline

n=int(input())
e=int(input())
visited=[False]*(n+1)
a=[[] for _ in range(n+1)]
result=[sys.maxsize]*(n+1)
q=PriorityQueue()

for i in range(e):
    x,y,tmp=map(int,input().split())
    a[x].append((y,tmp))

start,end=map(int,input().split())
result[start]=0
q.put((0,start))

while q.qsize()>0:
    now=q.get()
    target=now[1]
    if visited[target]:
        continue
    visited[target]=True
    for i in a[target]:
        next=i[0]
        tmp=i[1]
        if result[next]>result[target]+tmp:
            result[next]=result[target]+tmp
            q.put((result[next],next))

print(result[end])