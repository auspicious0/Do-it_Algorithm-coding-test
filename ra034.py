#백준 온라인 저지 1744번
from queue import PriorityQueue
#내가 푼 풀이 - 오답
# minus=PriorityQueue()
# plus=PriorityQueue()
# n=int(input())
# for i in range(n):
#     k=int(input())
#     minus.put(-k)
#     plus.put(k)
# sum_minus=0
# sum_plus=0

# while plus.qsize()>1:
#     x=plus.get()
#     y=plus.get()
#     if x<0 and y<0:
#         sum_plus+=x*y
#     elif x<0 and y==0:
#         continue
#     else:
#         break

# while minus.qsize()>1:
#     x=-minus.get()
#     y=-minus.get()
#     if x>2 and y>1:
#         sum_minus+=x*y
#     elif 0<=x<=2 or 0<=y<=2:
#         sum_minus+=(x+y)
#     else:
#         break
# print(sum_minus+sum_plus)

n=int(input())
plus=PriorityQueue()
minus=PriorityQueue()
one=0
zero=0
for i in range(n):
    x=int(input())
    if x>1:
        plus.put(-x)
    elif x==1:
        one+=1
    elif x==0:
        zero+=1
    else:
        minus.put(x)
sum=one
while plus.qsize()>1:
    x=plus.get()
    y=plus.get()
    sum+=x*y
if plus.qsize()>0:
    sum+=-plus.get()
while minus.qsize()>1:
    x=minus.get()
    y=minus.get()
    sum+=x*y
if minus.qsize()>0:
    if zero==0:
        sum+=minus.get()

print(sum)