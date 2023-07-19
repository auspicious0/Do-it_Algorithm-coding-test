#백준 온라인 저지 1850
#오답 메모리 초과 - 상당히 큰 수라는 것을 간과했다.
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# a,b=map(int,input().split())
# print(gcd(int('1'*a),int('1'*b)))
#정답코드
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b=map(int,input().split())
a,b=max(a,b),min(a,b)
print('1'*gcd(a,b))