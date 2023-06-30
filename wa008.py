n=int(input())
numbers=list(map(int,input().split()))
numbers.sort()
count=0

for i,v in enumerate(numbers):
    start_index=0
    end_index=n-1#리스트 안에 음수가 있을 수 있기 때문에 전 범위 조사

    while start_index<end_index:
        if numbers[start_index]+numbers[end_index]>v:
            end_index-=1
        elif numbers[start_index]+numbers[end_index]<v:
            start_index+=1
        else:
            if start_index!=i and end_index!=i:#리스트 안에 0이 있을 수 있기 때문 0+v=v
                count+=1
                break
            if start_index==i:
                start_index+=1
            if end_index==i:
                end_index-=1

print(count)
            