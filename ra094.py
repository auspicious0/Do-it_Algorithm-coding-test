#백준 온라인 저지 11049
import sys
input=sys.stdin.readline
n=int(input())
m=[(0,0)]
d=[[-1 for j in range(n+1)] for i in range(n+1)]

for i in range(n):
    x,y=map(int,input().split())
    m.append((x,y))

def execute(s,e):
    result=sys.maxsize
    if d[s][e]!=-1:
        return d[s][e]
    if s+1==e:
        return m[s][0]*m[e][0]*m[e][1]
    if s==e:
        return 0
    for i in range(s,e):
        result=min(result,execute(s,i)+execute(i+1,e)+m[s][0]*m[i][1]*m[e][1])
    d[s][e]=result
    return d[s][e]
print(execute(1,n))

