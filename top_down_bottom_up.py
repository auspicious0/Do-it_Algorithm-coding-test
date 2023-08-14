#top_down
import sys
input=sys.stdin.readline
n=int(input())
d=[-1]*n
d[0]=0
d[1]=1

def fibo(n):
    if d[n]!=-1:
        return d[n]
    d[n]=fibo(n-1)+fibo(n-2)
    return d[n]

#bottom_up
for i in range(2,n+1):
    d[i]=d[i-1]+d[i-2]
