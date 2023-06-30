n,l=map(int,input().split())
ai=list(map(int,input().split()))
d=[]
for i in range(n):
    d.append(min(ai[i-l+1:i+1]))
print(''.join(d))