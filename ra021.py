#병합정렬을 활용한 문제.
count=0
def merge(s,e):
    global count
    if e-s<1:
        return
    m=int(s+(e-s)/2)
    merge(s,m)
    merge(m+1,e)
    
    for i in range(s,e+1):
        num2[i]=num[i]

    k=s
    index1=s
    index2=m+1
    while index1<=m and index2<=e:
        if num2[index1]>num2[index2]:
            count+=index2-k
            num[k]=num2[index2]
            k+=1
            index2+=1

            
        else:
            num[k]=num2[index1]
            k+=1
            index1+=1
            
    while index1<=m:
        num[k]=num2[index1]
        k+=1
        index1+=1
    while index2<=e:
        num[k]=num2[index2]
        k+=1
        index2+=1

    

n=int(input())
num=list(map(int,input().split()))
num2=[0]*n
merge(0,n-1)
print(num)
print(count)