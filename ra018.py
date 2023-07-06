#삽입 정렬
# n=int(input())
# numbers=list(map(int,input().split()))
# numbers.sort()
# sum_=[]
# for i in range(n):
#     sum_.append(sum(numbers[:i+1]))
# print(sum(sum_))

n=int(input())
numbers=list(map(int,input().split()))

for i in range(1,n):
    t_i=i
    t_v=numbers[i]

    for j in range(i-1,-1,-1):
        if numbers[j] <t_v:
            t_i=j+1
            break
        if j==0:
            t_i=0
    
    for j in range(i,t_i,-1):
        numbers[j]=numbers[j-1]
    numbers[t_i]=t_v
sum=[0]*n
sum[0]=numbers[0]

sum_=0
for i in range(1,n):
    sum[i]=sum[i-1]+numbers[i]

for i in range(n):
    sum_+=sum[i]
print(sum_)