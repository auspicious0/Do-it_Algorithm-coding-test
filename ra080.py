# import sys
# input=sys.stdin.readline

# m=int(input())
# col_len=list(map(int,input().split()))
# n=sum(col_len)
# k=int(input())

# d=[[0 for j in range(n+1)] for i in range(n+1)]
# for i in range(n+1):
#     d[i][i]=1
#     d[i][0]=1
#     d[i][1]=i

# for i in range(3,n+1):
#     for j in range(2,i):
#         d[i][j]=d[i-1][j]+d[i-1][j-1]
# result=0
# for i in col_len:
#     if i>=k:
#         result+=d[i][k]
# print(result/d[n][k])

#다른 풀이

import sys
input=sys.stdin.readline
m=int(input())
color_len=list(map(int,input().split()))
k=int(input())
total=sum(color_len)
ans=0

for i in range(m):
    tmp=1
    if color_len[i]>=k:
        for j in range(k):
            tmp*=(color_len[i]-j)/(total-j)
        ans+=tmp
print(ans)