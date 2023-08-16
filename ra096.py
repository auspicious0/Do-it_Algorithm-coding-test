import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
num.insert(0,0)

d=[0]*(n+1)
b=[0]*(n+1)
a=[0]*(n+1)
b[1]=num[1]
d[1]=1
maxIndex=1
index=0

def binarySearch(l,r,v):
    while l<r:
        mid=(l+r)//2
        if b[mid]<v:
            l=mid+1
        else:
            r=mid
    return l
for i in range(2,n+1):
    if num[i]>b[maxIndex]:
        maxIndex+=1
        b[maxIndex]=num[i]
        d[i]=maxIndex
    else:
        index=binarySearch(1,maxIndex,num[i])
        b[index]=num[i]# 
        d[i]=index

print(maxIndex)
index=maxIndex
x=b[maxIndex]+1
for i in range(n,0,-1):
    if d[i]==index and num[i]<x:
       a[index]=num[i]
       x=num[i]
       index-=1

for i in range(1,maxIndex+1):
    print(a[i],end=" ") 