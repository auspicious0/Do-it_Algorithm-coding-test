from collections import deque

now=list(map(int,input().split()))
visited=[[False for _ in range(201)] for _ in range(201)]# true or false
give=[0,0,1,1,2,2]
receive=[1,2,0,2,0,1]
answer=[False]*201

def bfs():
    q=deque()
    q.append((0,0))
    visited[0][0]=True
    answer[now[2]]=True
    while q:
        A,B=q.popleft()
        C=now[2]-A-B
        for i in range(6):
            next=[A,B,C]#각 방법 마다 6가지 방향성을 나타냄
            next[receive[i]]+=next[give[i]]
            next[give[i]]=0#초기화 miss
            if next[receive[i]]>now[receive[i]]:
                next[give[i]]=next[receive[i]]-now[receive[i]]
                next[receive[i]]=now[receive[i]]
            if visited[next[0]][next[1]] == False:
                q.append((next[0],next[1]))
                visited[next[0]][next[1]]=True
                if next[0]==0:
                    answer[next[2]]=True
bfs()

for i in range(len(answer)):
    if answer[i]==True:
        print(i, end=' ')
