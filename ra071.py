n,m,k=map(int,input().split())
count=0
N=n
while N>0:
    count+=1
    N//=2
if n==int(2**(count-1)):
    count-=1
size=int(2**(count+1))
start=size//2-1
number=[0]*(size+1)
for i in range(start+1,start+n+1):
    number[i]=int(input())

def setNum(i):
    while i>1:
        number[i//2]+=number[i]
        i-=1
setNum(size-1)

def chageNum(index,value):
    index=start+index
    diff=value-number[index]
    while index>0:
        number[index]+=diff
        index//=2
def sumNum(s,e):
    s,e=start+s,start+e
    partSum=0
    while s<=e:  
        if s%2==1:
            partSum+=number[s]
            s+=1
        if e%2==0:
            partSum+=number[e]
            e-=1
        s//=2
        e//=2
    return partSum
for i in range(m+k):
    q,x,y=map(int,input().split())
    if q==1:
        chageNum(x,y)
    else:
        tmp=sumNum(x,y)
        print(tmp)
