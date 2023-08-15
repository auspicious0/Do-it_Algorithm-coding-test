import sys
input=sys.stdin.readline
n=int(input())
t=[0]*(n+1)
p=[0]*(n+1)
d=[0]*(n+2)

for i in range(1,n+1):
    t[i],p[i]=map(int,input().split())
for i in range(n,0,-1):
    if t[i]+i>n+1:
        d[i]=d[i+1]
    else:
        d[i]=max(d[i+1],d[i+t[i]]+p[i])
print(d[1])