from queue import PriorityQueue
import sys
input=sys.stdin.readline

n=int(input())
numbers=PriorityQueue()    

for i in range(n):
    k=int(input())
    if k==0:
        if numbers.empty():
            print(0)
        else:
            print(numbers.get()[1])
    else:
        numbers.put((abs(k),k))

        