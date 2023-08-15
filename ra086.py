import sys
input=sys.stdin.readline
n=int(input())
d=[0]*(n+1)
d[1]=1

for i in range(2,n+1):
    d[i]=d[i-1]+d[i-2]
print(d[n])
#dp테이블을 설정할 때 크기의 이슈를 잘 주목해야한다.
#초기값 세팅에 들어갈 인덱스 보다 
#dp테이블이 작을 수 있는 경우의 수를 판단해야 한다.!

#다른 풀이
import sys
input=sys.stdin.readline
n=int(input())
d=[[0 for j in range(2)] for i in range(n+1)]
d[1][1]=1
d[1][0]=0
for i in range(2,n+1):
    d[i][0]=d[i-1][0]+d[i-1][1]
    d[i][1]=d[i-1][0]
print(d[n][0]+d[n][1])