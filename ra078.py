#내가 생각한 직관적 풀이
# import sys
# input=sys.stdin.readline
# t=int(input())
# for _ in range(t):
#     k=int(input())
#     n=int(input())
#     d=[[0 for _ in range(n+1)] for _ in range(k+1)]
#     for i in range(1,n+1):
#         d[0][i]=i
#     for i in range(1,k+1):
#         for j in range(1,n+1):
#             d[i][j]=sum(d[i-1][:j+1])
#     print(d[k][n])
#정답 풀이
import sys
input=sys.stdin.readline
d=[[0 for j in range(15)] for i in range(15)]

for i in range(1,15):
    d[0][i]=i
    d[i][1]=1

for i in range(1,15):
    for j in range(2,15):
        d[i][j]=d[i][j-1]+d[i-1][j]

for i in range(int(input())):
    a=int(input())
    b=int(input())
    print(d[a][b])