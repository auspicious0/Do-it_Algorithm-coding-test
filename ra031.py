#백준 문제 1300번
#내가 푼 방법 (오답)
# n=int(input())
# num=[]
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         num.append(i*j)
# k=int(input())
# print((k//n+1)*(k%n+1))

n=int(input())
k=int(input())
ans=0
start=1
end=k
while start<=end:
    mid=int((start+end)/2)
    cnt=0
    for i in range(1,n+1):
        cnt+=min(int(mid/i),n)
    if cnt<k:
        start=mid+1
    else:
        ans=mid
        end=mid-1
print(ans)
