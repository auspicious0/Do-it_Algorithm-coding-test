#백준 온라인 저지 1033번
n=int(input())
visited=[False]*(n)
ratis=[[] for _ in range(n)]
d=[0]*n
lcm=1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def dfs(v):
    visited[v]=True
    for i in ratis[v]:
        next=i[0]
        if not visited[next]:
            d[next]=d[v]*i[2]//i[1]
            dfs(next)

for i in range(n-1):
    a,b,p,q=map(int,input().split())
    ratis[a].append((b,p,q))
    ratis[b].append((a,q,p))
    lcm*=(p*q//gcd(p,q))


d[0]=lcm
dfs(0)
gcd_=d[0]

for i in range(1,n):
    gcd_=gcd(gcd_,d[i])
for i in range(n):
    print(int(d[i]//gcd_),end=" ")