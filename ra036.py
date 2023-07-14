#백준 온라인 져지 1541번
#문제를 명확히 이해하지 못한 풀이 즉 괄호의 존재에 대한 의미를 파악하지 못함
# import re
# s=input()
# minus=0
# for i in s:
#     if i=='-':
#         minus+=1
# s=list(map(int,re.split('[+-]',s)))#re.split('[^0-9]') 숫자가 아닌 하나 이상의 문자를 구분자로
# s.sort(reverse=True)
# print(-sum(s[:minus])+sum(s[minus:]))
s=list(input().split('-'))
result=0
if len(s)==1:
    print(sum(list(map(int,s[0].split('+')))))
else:
    result=sum(list(map(int,s[0].split('+'))))
    for i in range(1,len(s)):
        result-=sum(list(map(int,s[i].split('+'))))
    print(result)