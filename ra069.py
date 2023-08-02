import sys
input=sys.stdin.readline
n,m=map(int,input().split())
string1=set()
num=0
for i in range(n):
    string1.add(input())
for i in range(m):
    string2=input()
    if string2 in string1:
        num+=1
print(num)

