#백준 온라인 저지 11047번
n,k=map(int,input().split())
num=[0]*n

for i in range(n):
    num[i]=int(input())

count=0
#나의 풀이
# while True:
#     if k%num[-1]==0:
#        count+=k//num[-1]
#        break 
#     else:
#         count+=k//num[-1]
#         k=k%num[-1]
#         num.pop()

#저자의 풀이
for i in range(n-1,-1,-1):
    if num[i] <=k:
        count+=k//num[i]
        k%=num[i]

print(count)