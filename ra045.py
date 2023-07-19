#백준 온라인 저지 21568번

a,b,c=map(int,input().split())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def execute(a,b):
    ret=[0]*2
    if b==0:
        ret[0]=1
        ret[1]=0
        return ret
    k=a//b
    v=execute(b,a%b)
    ret[0]=v[1]
    ret[1]=v[0]-v[1]*k
    return ret

gcd_=gcd(a,b)

if c%gcd_==0:
    k=c//gcd_
    v=execute(a,b)
    print(k*v[0],end=" ")
    print(k*v[1])
else:
    print(-1)