#sort를 이용한 풀이
import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input())
numbers=[0]*n
for i in range(n):
    numbers[i]=int(input())
numbers.sort()
for i in numbers:
    print(str(i)+"\n")