#내가 생각한 방법 1
# n,k=map(int,input().split())
# sum=1
# result=1
# if k==0:
#     print(1)
# else:
#     while k!=0:
#         sum*=k
#         k-=1
#         result*=n
#         n-=1
#     print(int(result/sum))

#내가 생각한 방법 2
# from itertools import combinations
# n,k=map(int,input().split())
# tmp=[i for i in range(n)]
# print(len(list(combinations(tmp,k))))

#답풀이 중 애매한 논리 수정
n,k=map(int,input().split())
d=[[0 for j in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    d[i][0]=1
    d[i][1]=i
    d[i][i]=1
for i in range(2,n+1):
    for j in range(2,i):
        d[i][j]=d[i-1][j]+d[i-1][j-1]
print(d[n][k])