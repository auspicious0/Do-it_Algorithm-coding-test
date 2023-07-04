# 정렬을 이용한 풀이1
# import sys
# print=sys.stdout.write
# input=sys.stdin.readline
# n=int(input())
# numbers=[0]*n
# for i in range(n):
#     numbers[i]=int(input())
# for i in range(n):
#     for j in range(i,n):
#         if numbers[i]>numbers[j]:
#             numbers[i],numbers[j]=numbers[j],numbers[i]
# for i in numbers:
#     print(str(i)+"\n")
# 버블 정렬을 이용한 풀이
n=int(input())
numbers=[0]*n
for i in range(n):
    numbers[i]=int(input())
for i in range(n-1):
    for j in range(n-1-i):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
for i in numbers:
    print(i)