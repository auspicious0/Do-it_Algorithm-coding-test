#wrong answer 시간 초과

m,n=map(int,input().split())
sum_list=list(map(int,input().split()))
count=0
for i in range(m):
    for j in range(i,m):
        bool_sum=sum(sum_list[i:j+1])%3
        if bool_sum==0:
            count+=1
print(count)