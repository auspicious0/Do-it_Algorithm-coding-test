n=int(input())
m=int(input())
numbers=list(map(int,input().split()))
numbers.sort()

start_index=0
end_index=n-1
count=0

while start_index<end_index:
    if numbers[start_index]+numbers[end_index]>m:
        end_index-=1
    elif numbers[start_index]+numbers[end_index]==m:
        count+=1
        start_index+=1
        end_index-=1
    else:
        start_index+=1

print(count)