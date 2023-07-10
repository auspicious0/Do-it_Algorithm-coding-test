#백준 온라인 져지 2023
import sys
import math
sys.setrecursionlimit(100000)
input=sys.stdin.readline
k=int(input())
#에라토스테네스의 체
# n=10**k-1
# array=[True for i in range(n+1)]

# for i in range(2,int(math.sqrt(n))+1):
#     if array[i]==True:
#         j=2
#         while i*j<=n:
#             array[i*j]=False
#             j+=1
def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
def DFS(x):
    if len(str(x))==k and isPrime(x):
        print(x)
        return
    if isPrime(x)==True:        
        for i in range(1,10,2):
            DFS(x*10+i)
DFS(2)
DFS(3)
DFS(5)
DFS(7)
