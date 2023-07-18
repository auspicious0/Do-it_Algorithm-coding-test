#백준 온라인 저지 1456번
a,b=map(int,input().split())
num=[True]*(10000001)
num[0]=num[1]=False

for i in range(2,int(len(num)**0.5)+1):
    if num[i]==True:
        for j in range(i*2,len(num),i):
            num[j]=False
count=0
for i in range(2,len(num)):
    if num[i]==True:
        temp=i
        while i<=b/temp:
            if i>=a/temp:
                count+=1
            temp*=i
print(count)