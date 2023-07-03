from collections import deque
n=int(input())
numbers_p1=[]
numbers_m1=[]
numbers_p=deque([])
numbers_m=deque([])
for i in range(n):
    a=int(input())
    if a==0:
        if numbers_p or numbers_m:
            if numbers_p and numbers_m:
                if abs(numbers_p[0]) <abs(numbers_m[0]):
                    print(numbers_p.popleft())
                else:
                    print(numbers_m.popleft())
            elif numbers_p:
                print(numbers_p.popleft())
            else:
                print(numbers_m.popleft())
        else:
            print(0)
                
    elif a>0:
        numbers_p1.append(a)
        numbers_p1.sort()
        numbers_p=deque(numbers_p1)
    else:
        numbers_m1.append(a)
        numbers_m1.sort()
        numbers_m=deque(numbers_m1)
