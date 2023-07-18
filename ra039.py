n=int(input())
num=[0]*(10000001)
num[0]=num[1]=1
for i in range(2,int(len(num)**0.5)+1):
    if num[i]==0:
        for j in range(i*2,len(num),i):
            num[j]=1
for i in range(n,len(num)):
    if num[i]==0:
        if len(str(i))==1:
            print(i)
            break
        temp=str(i)
        if temp==temp[::-1]:
            print(i)
            break
