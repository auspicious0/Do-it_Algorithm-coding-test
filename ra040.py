#백준 온라인 저지 1016번#
#오답풀이
# Min,Max=map(int,input().split())
# count=Max-Min+1
# num=[0]*count
# for i in range(count):
#     num[i]=Min+i
# for i in range(2,1000000+1):
#     tmp=i*i
#     if tmp>Max:
#         break
#     for j in range(count):
#         if num[j]%tmp==0:
#             num[j]=0
# count=0
# for i in num:
#     if i!=0:
#         count+=1
# print(count)
#정답

Min,Max=map(int,input().split())
check=[False]*(Max-Min+1)
for i in range(2,int(Max**0.5)+1):
    start_index=int(Min/(i*i))
    if Min%(i*i)!=0:
        start_index+=1
    for j in range(start_index,int(Max/(i*i))+1):
        check[int((i*i)*j-Min)]=True
cnt=0
for i in check:
    if not i:
        cnt+=1
print(cnt)