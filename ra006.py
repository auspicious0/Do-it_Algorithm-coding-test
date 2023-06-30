#two pointer 로 시관초과 해결
n=int(input())
count=1
sum=1
start_index=1
end_index=1
while end_index!=n:
    if sum>n:
        sum-=start_index
        start_index+=1
    elif sum==n:
        count+=1
        end_index+=1
        sum+=end_index
    else:
        end_index+=1
        sum+=end_index
print(count)