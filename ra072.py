import sys
input=sys.stdin.readline
n,m=map(int,input().split())
N=n
count=0
while N>0:
    count+=1
    N//=2
size=int(2**(count+1))
start=int(2**count)-1
tree=[0]*size

for i in range(start+1,start+1+n):
    tree[i]=int(input())


def setTree(i):
    while i>2:
        tree[i//2]=min(tree[i],tree[i-1])
        i-=2
setTree(size-1)

def findMin(s,e):
    treeMin=1000000001
    global start
    s,e=start+s,start+e
    while s<=e:
        if s%2==1:
            treeMin=min(treeMin,tree[s])
            s+=1
        if e%2==0:
            treeMin=min(treeMin,tree[e])
            e-=1
        s//=2
        e//=2
    return treeMin
for i in range(m):
    a,b=map(int,input().split())
    print(findMin(a,b))
