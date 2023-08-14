import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
dp=[[0 for j in range(201)] for i in range(201)]
for i in range(201):
    dp[i][0]=1
    dp[i][i]=1
    dp[i][1]=i
for i in range(3,201):
    for j in range(2,i):
        dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
if dp[n+m][m]<k:
    print(-1)
else:
    for _ in range(m+n):
        if dp[n+m-1][m]>=k:
            print('a',end='')
            n-=1
        else:
            k-=dp[n+m-1][m]
            print('z',end='')
            m-=1