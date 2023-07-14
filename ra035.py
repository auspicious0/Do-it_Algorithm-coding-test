#백준 온라인 져지 1931번

n=int(input())
num=[[0]*2 for i in range(n)]
for i in range(n):
    start,end=map(int,input().split())
    num[i][0]=end #sort 를 위해 end를 먼저
    num[i][1]=start
num.sort()
end=-1
count=0
for i in range(n):
    if num[i][1]>=end: #start가 end 이후라면 count+=1
        end=num[i][0]
        count+=1
print(count)