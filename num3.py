n,m=input().split()
numbers=list(map(int,input().split()))
num_=[0]*len(numbers)
for i in range(len(numbers)):
    num_[i]=sum(numbers[:i+1])
for i in range(int(m)):
    x,y=input().split()
    if int(x)==1:
        print(num_[int(y)-1])
    else:
        print(num_[int(y)-1]-num_[int(x)-2])#x값이 0보다 작아지는 지점에서 이슈가 발생 -> ifelse처리 해야함

#내 풀이, 오답 시간초과.
