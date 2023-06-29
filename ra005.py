#wrong answer 005 ->right answer 005
#슈도코드를 확인하고 코드를 작성했지만 틀렸다
#오랜 시간 고민한 끝에 두 가지 부분에서 잘못 작성한 부분이 있었다.
#머릿 속으로 하는 디버깅에 집중하자
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
li=list(map(int,input().split()))
temp=0
count=0
n_li=[0]*n

for i in range(m):
    temp+=li[i]
    k=temp%n
    if k==0:
        count+=1
    n_li[k]+=1

for i in range(n):
    if n_li[i]>1:
        count+=(n_li[i]*(n_li[i]-1)//2) 
print(count)