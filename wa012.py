n=int(input())
numbers=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if numbers[i]<numbers[j]:
            print(numbers[j],end=' ')
            break
    else:
        print(-1,end=' ')
