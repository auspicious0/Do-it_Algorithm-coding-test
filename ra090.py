import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

a=list(map(str,input()))
a.pop()
b=list(map(str,input()))
b.pop()

lcs_num=[[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
path=[]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            lcs_num[i][j]=lcs_num[i-1][j-1]+1
        else:
            lcs_num[i][j]=max(lcs_num[i-1][j],lcs_num[i][j-1])

print(lcs_num[len(a)][len(b)])

def LCS(r,c):
    if r==0 or c==0:
        return
    if a[r-1]==b[c-1]:
        path.append(a[r-1])
        LCS(r-1,c-1)
    else:
        if lcs_num[r-1][c]>lcs_num[r][c-1]:
            LCS(r-1,c)
        else:
            LCS(r,c-1)
LCS(len(a),len(b))
for i in range(len(path)-1,-1,-1):
    print(path[i],end='')
print()