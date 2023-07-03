from collections import deque
numbers=deque([i for i in range(1,int(input())+1)])
i=2
while len(numbers)!=1:
    if i%2==0:
        numbers.popleft()
        i+=1
    else:
        a=numbers.popleft()
        numbers.append(a)
        i+=1
print(numbers.pop())