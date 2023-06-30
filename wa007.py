n=int(input())
m=int(input())
numbers=list(map(int,input().split()))
numbers.sort()

start_index=0
end_index=0
count=0
sum=0

while end_index!=n:
    if sum>m:
        sum-=numbers[start_index]
        start_index+=1
    elif sum==m:
        count+=1
        end_index+=1
        if end_index==n:
            break
        sum+=numbers[end_index]
    else:
        end_index+=1
        if end_index==n:
            break
        sum+=numbers[end_index]

print(count)