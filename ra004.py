#D[i][j]=D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i][j] 2차원 배열의 구간합 만들기
#D[x2][y2]-D[x2][y1-1]-D[x1-1][y2]+D[x1-1][y1-1] 2차원 배열의 구간합을 통해 값 구하기

import sys
input=sys.stdin.readline
k,l=map(int,input().split())
A,M=[[0]*(k+1)],[[0]*(k+1) for i in range(k+1)]

for i in range(k):
    A_row=[0]+[int(j) for j in input().split()]
    A.append(A_row)

for i in range(1,k+1):
    for j in range(1,k+1):
        M[i][j]=M[i][j-1]+M[i-1][j]-M[i-1][j-1]+A[i][j]

for _ in range(l):
    x1,y1,x2,y2=map(int,input().split())
    result=M[x2][y2]-M[x2][y1-1]-M[x1-1][y2]+M[x1-1][y1-1]
    print(result)