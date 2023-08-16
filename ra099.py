import sys
input=sys.stdin.readline
n=int(input())
parent=[-1]*(n+1)

def ccw(x1,y1,x2,y2,x3,y3):
    tmp= (x1*y2+x2*y3+x3*y1)-(x1*y3+x3*y2+x2*y1)
    if tmp<0:
        return -1
    elif tmp>0:
        return 1
    return 0
def isOverlap(x1,y1,x2,y2,x3,y3,x4,y4):
    if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2) and min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1,y2):
        return True
    else:
        return False
def cross(x1,y1,x2,y2,x3,y3,x4,y4):
    abc=ccw(x1,y1,x2,y2,x3,y3)
    abd=ccw(x1,y1,x2,y2,x4,y4)
    cda=ccw(x3,y3,x4,y4,x1,y1)
    cdb=ccw(x3,y3,x4,y4,x2,y2)

    if abc*abd==0 and cda*cdb==0:
        return isOverlap(x1,y1,x2,y2,x3,y3,x4,y4)
    elif abc*abd<=0 and cda*cdb<=0:
        return True
    return False
def find(a):
    if parent[a]<0:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    else:
        parent[a]+=parent[b]
        parent[b]=a
l=[0 for i in range(n+1)]
for i in range(1,n+1):
    l[i]=list(map(int,input().split()))
    for j in range(1,i):
        if cross(l[i][0],l[i][1],l[i][2],l[i][3],l[j][0],l[j][1],l[j][2],l[j][3]):
            union(i,j)
ans=0
result=0
for i in range(1,n+1):
    if parent[i]<0:
        ans+=1
        result=min(result,parent[i])
print(ans)
print(-result)