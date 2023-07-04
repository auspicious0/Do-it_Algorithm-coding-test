# n=list(map(int,input()))
# k=len(n)

# for i in range(k):
#     for j in range(i+1,k):
#         if n[i]<n[j]:
#             n[i],n[j]=n[j],n[i]
# n=list(map(str,n))
# print(''.join(n))
n=list(input())
k=len(n)
for i in range(k):
    Max=i
    for j in range(i+1,k): 
        if n[j] >n[Max]:
            Max=j
    if n[i]< n[Max]:
        n[i],n[Max]=n[Max],n[i]
for i in n:
    print(i,end="")