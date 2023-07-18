#백준 온라인 저지 1929번
import sys
import math
input=sys.stdin.readline
print=sys.stdout.write
m,n=map(int,input().split())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,int(math.pow(n,0.5))+1):
    if dp[i]==0:
        for k in range(i*2,n+1,i):
            dp[k]=1

for i in range(m,n+1):
    if dp[i]==0:
        print(str(i)+'\n')
        