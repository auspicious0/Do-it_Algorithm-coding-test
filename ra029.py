import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
num.sort()

def search_2(s,e,k):
    mid=int((s+e)/2)
    if s>e:#범위 및 종료조건 확인
        return False
    if num[mid]==k:
        return True
    elif num[mid]>k:
        return search_2(s,mid-1,k)
    else:
        return search_2(mid+1,e,k)

t=int(input())
target=list(map(int,input().split()))
for i in range(t):
    if search_2(0,n-1,target[i])==True:
        print(1)
    else:
        print(0)