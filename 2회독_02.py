n=int(input())
num=list(map(int,input().split()))
k=1/max(num)*100
print(sum(num)/len(num)*k)