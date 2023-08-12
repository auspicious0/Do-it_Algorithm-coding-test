import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
N=n
count=0
MOD=1000000007
while N>0:
    count+=1
    N//=2

size=int(2**(count+1))
start=int(2**(count))-1
tree=[1]*size

for i in range(start+1,start+1+n):
    tree[i]=int(input())

def setTree(i):
    while i>1:
        tree[i//2]=tree[i//2]*tree[i]%MOD
        i-=1
setTree(size-1)

def changeTree(index,value):
    global start
    index=start+index
    tree[index]=value
    while index>0:
        index//=2
        tree[index]=tree[index*2]*tree[index*2+1]%MOD

def mulTree(s,e):
    global start
    s,e=start+s,start+e
    treeMul=1
    while s<=e:
        if s%2==1:
            treeMul=treeMul*tree[s]%MOD
            s+=1
        if e%2==0:
            treeMul=treeMul*tree[e]%MOD
            e-=1
        s//=2
        e//=2
    return treeMul

for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        changeTree(b,c)
    else:
        print(mulTree(b,c))