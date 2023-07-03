n=int(input())
numbers=[0]*n
for i in range(n):
    numbers[i]=int(input())
result=True
cnt=1
answer=''
stack=[]

for i in range(n):
    su=numbers[i]
    if su>=cnt:
        while su>=cnt:
            stack.append(cnt)
            cnt+=1
            answer+="+\n"
        stack.pop()
        answer+="-\n"
    else:
        target=stack.pop()
        if su<target:
            result=False
            print('NO')
            break
        else:
            answer+="-\n"
if result:
    print(answer)
