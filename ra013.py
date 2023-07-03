from collections import deque
numbers=deque([i for i in range(1,int(input())+1)])
while len(numbers)!=1:
    numbers.popleft()    
    a=numbers.popleft()
    numbers.append(a)
print(numbers.pop())