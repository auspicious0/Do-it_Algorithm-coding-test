import sys
input=sys.stdin.readline
n=int(input())
a=[0]*n
for i in range(n):
    a[i]=(int(input()),i)
a_sort=sorted(a)

MAX=0
for i in range(n):
    if MAX<a_sort[i][1]-i:
        MAX=a_sort[i][1]-i
print(MAX+1)