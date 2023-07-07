#백준 온라인 저지 10989번
#계수 정렬을 이용한 문제
#기수 정렬 알고리즘
import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(10000+1)

for i in range(n):
    dp[int(input())]+=1
for i in range(10001):
    if dp[i]!=0:
        for j in range(dp[i]):
            print(i)


# from collections import deque

# def radix_sort(nums):
#     buckets = [deque() for _ in range(10)]

#     max_val = max(nums)
#     Q = deque(nums)
#     cur_ten = 1

#     while max_val >= cur_ten:
#         while Q:
#             num = Q.popleft()
#             buckets[(num // cur_ten) % 10].append(num)

#         for bucket in buckets:
#             while bucket:
#                 Q.append(bucket.popleft())

#         cur_ten *= 10

#     return list(Q)


# print(radix_sort([15, 27, 64, 25, 50, 17, 39, 28]))
        