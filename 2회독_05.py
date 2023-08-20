n,m=map(int,input().split())
num=list(map(int,input().split()))
s=[0]*(n)
c=[0]*(m)
result=0
for i in range(n):
    s[i]=s[i-1]+num[i]

for i in range(n):
    c[s[i]%m]+=1

result+=c[0]

for i in range(m):
    result+=c[i]*(c[i]-1)//2
print(result)