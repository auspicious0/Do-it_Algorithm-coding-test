n=int(input())
k=1
count=1
while True:
    if k==n:
       break
    temp=0
    for i in range(k,n):
        temp+=i
        if temp==n:
            count+=1
    k+=1
print(count)