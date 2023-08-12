n,m,k=map(int,input().split())
N=n
count=0
while N>0:
    count+=1
    N//=2
size=int(2**(count+1))
number=[0]*size
start=int(2**count)-1
for i in range(start+1,start+1+n):
    number[i]=int(input())

def setNum(l):
    while l!=1:
        number[l//2]+=number[l]
        l-=1
setNum(size-1)

def changeNum(index,value):
    global start
    index=index+start
    diff=value-number[index]
    while index>0:
        number[index]+=diff
        index//=2

def sumNum(s,e):
    global start
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
    a,b,c=map(int,input().split())
    if a==1:
        changeNum(b,c)
    else:
        print(sumNum(b,c))
    