import sys
input=sys.stdin.readline
print=sys.stdout.write
def merge(s,e):
    if e-s<1:
        return
    m=int(s+(e-s)/2)
    merge(s,m)
    merge(m+1,e)
    for i in range(s,e+1):
        a[i]=num[i]
    k=s
    index1=s
    index2=m+1
    while index1<=m and index2<=e:
        if a[index1]< a[index2]:
            num[k]=a[index1]
            k+=1
            index1+=1
        else:
            num[k]=a[index2]
            k+=1
            index2+=1
    while index1<=m:
        num[k]=a[index1]
        k+=1
        index1+=1
    while index2<=e:
        num[k]=a[index2]
        k+=1
        index2+=1
n=int(input())
num=[0]*(n+1)
a=[0]*(n+1)
for i in range(1,n+1):
    num[i]=int(input())
merge(1,n)
for i in range(1,n+1):
    print(str(num[i])+"\n")
