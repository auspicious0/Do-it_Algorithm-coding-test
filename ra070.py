n=int(input())
tree={}
for _ in range(n):
    root,left,right=input().split()
    tree[root]=[left,right]

def preOrder(alpha):
    if alpha=='.':
        return
    print(alpha,end='')
    preOrder(tree[alpha][0])
    preOrder(tree[alpha][1])

def inOrder(alpha):
    if alpha=='.':
        return
    inOrder(tree[alpha][0])
    print(alpha,end='')
    inOrder(tree[alpha][1])
def postOrder(alpha):
    if alpha=='.':
        return
    postOrder(tree[alpha][0])
    postOrder(tree[alpha][1])
    print(alpha,end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
print()


