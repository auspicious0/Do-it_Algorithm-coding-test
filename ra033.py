#백준 온라인 저지 1715번 문제
from queue import PriorityQueue
n=int(input())
q=PriorityQueue()
for i in range(n):
    x=int(input())
    q.put(x)
sum=0
while q.qsize()>1:
    x=q.get()
    y=q.get()
    temp=x+y
    sum+=temp
    q.put(temp)
print(sum)