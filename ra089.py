import sys
input=sys.stdin.readline

n=int(input())
number=list(map(int,input().split()))

left=[0]*(n)
right=[0]*(n)
result=number[0]
left[0]=number[0]
right[n-1]=number[n-1]

for i in range(1,n):
    left[i]=max(number[i],number[i]+left[i-1])
    result=max(left[i],result)

for i in range(n-2,-1,-1):
    right[i]=max(number[i],right[i+1]+number[i])

for i in range(1,n-1):
    tmp=left[i-1]+right[i+1]
    result=max(tmp,result)

print(result)