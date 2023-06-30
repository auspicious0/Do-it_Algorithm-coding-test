import itertools

m,n=map(int,input().split())
s=list(map(str,input()))
dnastr=[('A',0),('C',0),('G',0),('T',0)]
dna=list(map(int,input().split()))
s.sort()

for i in s:
    for j in dnastr:
        if i==j[0]:
            j[1]+=1
result=1
for i in range(4):
    if dnastr[i][1]<dna[i]:
        result=0
        break
    k=len(list(itertools.combinations(dnastr[i][1],dna[i])))
    result*=k
    n-=k
if n>0:
    #도저히 모르겠다!

