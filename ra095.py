import sys
input=sys.stdin.readline
n=int(input())
m=[0 for i in range(n)]
d=[[0 for j in range(1<<n)] for i in range(n)]

for i in range(n):
    m[i]=list(map(int,input().split()))

def tsp(c,v):
    if v==(1<<n)-1:
        if m[c][0]==0:
            return sys.maxsize
        else:
            return m[c][0]
    if d[c][v]!=0:
        return d[c][v]
    min_value=sys.maxsize
    for i in range(n):
        if m[c][i]!=0 and v&(1<<i)==0:
            min_value=min(min_value,tsp(i,v|(1<<i))+m[c][i])
    d[c][v]=min_value
    return min_value
print(tsp(0,1))