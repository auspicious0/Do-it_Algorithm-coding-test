#permutations 함수는 메모리가 초과된다.
# from itertools import permutations
# import sys
# input=sys.stdin.readline
# print=sys.stdout.write
# n=int(input())
# num=[i for i in range(1,n+1)]
# target=list(permutations(num,n))
# result=list(map(int,input().split()))
# if result[0]==1:
#     for i in target[result[1]-1]:
#         print(str(i)+" ")
# else:
#     print(str(target.index(tuple(result[1:]))+1))

import sys
input=sys.stdin.readline
n=int(input())
visited=[False]*21
f=[0]*21
s=[]
f[0]=1
for i in range(1,21):
    f[i]=f[i-1]*i

input_list=list(map(int,input().split()))
if input_list[0]==1:
    k=input_list[1]
    for i in range(1,n+1):
        cnt=1
        for j in range(1,n+1):
            if visited[j]==True:
                continue
            if k<=cnt*f[n-i]:
                k-=(cnt-1)*f[n-i]
                visited[j]=True
                s.append(j)
                break
            cnt+=1
    for i in s:
        print(i, end=" ")
else:
    k=1
    for i in range(1,n+1):
        cnt=0
        for j in range(1,input_list[i]):
            if not visited[j]:
                cnt+=1
        k+=cnt*f[n-i]
        visited[input_list[i]]=True
    print(k)

            