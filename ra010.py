from collections import deque

m,n=map(int,input().split())
numbers=list(map(int,input().split()))
deq=deque()

for i in range(len(numbers)):
    while deq and deq[-1][0]>=numbers[i]:
        deq.pop()
    deq.append((numbers[i],i))
    if deq[0][1]<=i-n:
        deq.popleft()
    print(deq[0][0],end=' ')
