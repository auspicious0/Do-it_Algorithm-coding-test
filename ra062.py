n=int(input())
floid=[0 for i in range(n)]

for i in range(n):
    floid[i]=list(map(int,input().split()))
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if floid[i][j]==1:
                continue
            else:
                if floid[i][k]==1 and floid[k][j]==1:
                    floid[i][j]=1
for i in range(n):
    for j in range(n):
        print(floid[i][j],end=' ')
    print()