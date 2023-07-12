#백준 2343번
n,m=map(int,input().split())
num=list(map(int,input().split()))
start,end=0,sum(num)#start,end를 잘 선택해야 하는 문제 함부로 sortx
for i in num:
    if start <i:
        start=i

while start<=end:
    mid=int((start+end)/2)
    count=1
    sum_=0
    for i in range(n):
        if num[i]+sum_>mid:
            count+=1
            sum_=0
        sum_+=num[i]

    if count>m:
        start=mid+1
    else:
        end=mid-1
print(start)
#wrong answer part
# def search_2(s,e):
#     if s>e:
#         return s
#     target=int((s+e)/2)
#     sum_=0
#     count=1
#     for i in range(n):
#         if sum_+num[i]>target:
#             sum_=0
#             count+=1
#         sum_+=num[i]
#     if count >m:
#         return search_2(target+1,e)
#     else:
#         return search_2(s,target-1)


