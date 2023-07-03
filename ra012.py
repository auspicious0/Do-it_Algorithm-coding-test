#오큰수 구하기
#lifo구조를 활용한 문제
n=int(input())
numbers=list(map(int,input().split()))
result=[-1]*n
stack=[]
for i in range(n):
    while stack and numbers[stack[-1]]<numbers[i]:
        result[stack.pop()]=numbers[i]
    stack.append(i)
for i in result:
    print(i,end=" ")
