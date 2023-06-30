#9 8
#cctgaser
#2 0 1 1
#acgt

check=[0]*4
insert=[0]*4
require=0

def add(p):
    global check,insert,require
    
    if p=='A':
        check[0]+=1
        if check[0]==insert[0]:
            require+=1
    elif p=='C':
        check[1]+=1
        if check[1]==insert[1]:
            require+=1
    elif p=='G':
        check[2]+=1
        if check[2]==insert[2]:
            require+=1
    else:
        check[3]+=1
        if check[3]==insert[3]:
            require+=1

def myremove(p):
    global check, insert, require

    if p=='A':
        if check[0]==insert[0]:
            require-=1
        check[0]-=1
    elif p=='C':
        if check[1]==insert[1]:
            require-=1
        check[1]-=1
    elif p=='G':
        if check[2]==insert[2]:
            require-=1
        check[2]-=1
    else:
        if check[3]==insert[3]:
            require-=1
        check[3]-=1

m,n=map(int,input().split())
s=input()
insert=list(map(int,input().split()))
count=0

for i in range(4):
    if insert[i]==0:
        require+=1

for i in range(n):
    add(s[i])

if require==4:
    count+=1

for i in range(n,m):
    j=i-n
    add(s[i])
    myremove(s[j])
    if require==4:
        count+=1
print(count)