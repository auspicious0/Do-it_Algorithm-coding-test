#백준 온라인 저지 1934번
# 정답 내 풀이
# def gcd(a,b):
#     if  b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# n=int(input())
# for i in range(n):
#     a,b=map(int,input().split())
#     a,b=max(a,b),min(a,b)
#     tmp=gcd(a,b)
#     print(tmp*a//tmp*b//tmp)
#답지
def gcd(a,b):
    if b==0:
        return a
    if a>b:
        c=a%b
        return gcd(b,c)
    else:
        c=b%a
        return gcd(a,c)
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    a,b=max(a,b),min(a,b)
    tmp=gcd(a,b)
    print(tmp*a//tmp)