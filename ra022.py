#백준 온라인 저지 10989번
#계수 정렬을 이용한 문제
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
        
