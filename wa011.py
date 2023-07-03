n=int(input())
numbers=[]
for i in range(n):
    numbers.append(int(input()))
sorted_numbers=sorted(numbers)
stack=[sorted_numbers[0]]
i=0
j=1
result=['+']

while stack:
    if stack[-1]==numbers[i]:
        i+=1
        stack.pop()
        result.append('-')
    else:
        stack.append(sorted_numbers[j])
        j+=1
        result.append('+')

if len(result)!=2*len(numbers):
    print('NO')
else:
    for i in result:
        print(i)


    
