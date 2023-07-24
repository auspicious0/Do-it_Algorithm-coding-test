n,m=map(int,input().split())
parent=[i for i in range(n+1)]
check_num=[]

def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a
def check(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return True
    else:
        return False
truep=list(map(int,input().split()))
trues=truep[0]
del truep[0]

for i in range(m):
    party=list(map(int,input().split()))
    for j in range(1,len(party)-1):
        union(party[j],party[j+1])
    check_num.append(party[1])
result=0
for i in range(len(check_num)):
    checknumber=1
    for j in range(trues):
        if check(truep[j],check_num[i]):
            checknumber=0
            break
    
    if checknumber==1:
        result+=1
print(result)