#right answer
import sys
input=sys.stdin.readline
n,m=map(int,input().split())#map함수를 통해 직관적으로 일반화
numbers=list(map(int,input().split()))
temp=0
tempnum=[0]#문제를 보면 인덱스 1부터 시작.
for i in range(n):
    temp+=numbers[i]#o(n)시간 복잡도 확보.
    tempnum.append(temp)
for i in range(m):
    x,y=map(int,input().split())
    print(tempnum[y]-tempnum[x-1])
