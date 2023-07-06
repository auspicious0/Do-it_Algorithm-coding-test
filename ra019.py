# n,k=map(int,input().split())
# num=list(map(int,input().split()))
# num.sort()
# print(num[k-1])
n,k=map(int,input().split())
num=list(map(int,input().split()))

def swap(i,j):
    global num
    num[i],num[j]=num[j],num[i]

def quicksort(s,e,k):
    global num
    if s<e:
        pivot=demand(s,e)
        if pivot>k:
            quicksort(s,pivot-1,k)
        elif pivot<k:
            quicksort(pivot+1,e,k)
        else:
            return 

def demand(s,e):
    global num
    if s+1==e:
        if num[s]>num[e]:
            swap(s,e)
        return e

    pivot=(s+e)//2
    swap(s,pivot)
    pivot=num[s]
    
    i=s+1
    j=e

    while i<=j:
        while pivot<num[j] and 0<j:
            j-=1
        while pivot>num[i] and i <len(num)-1:
            i+=1
        if i<=j:
            swap(i,j)
            i+=1
            j-=1
    num[s],num[j]=num[j],num[s]
    return j
quicksort(0,n-1,k-1)
print(num[k-1])