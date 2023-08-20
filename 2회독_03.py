import sys
input=sys.stdin.readline
print=sys.stdout.write
n,m=map(int,input().split())
num=list(map(int,input().split()))
s=[0]*(n+1)
for i in range(1,n+1):
    s[i]=s[i-1]+num[i-1]
for i in range(m):
    x,y=map(int,input().split())
    print(str(s[y]-s[x-1])+'\n')