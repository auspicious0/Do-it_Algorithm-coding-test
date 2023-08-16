import sys
input=sys.stdin.readline
x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    tmp=(x1*y2+x2*y3+x3*y1)-(x1*y3+x3*y2+x2*y1)
    if tmp>0:
        return 1
    elif tmp<0:
        return -1
    return 0
def isEnvelope(x1,y1,x2,y2,x3,y3,x4,y4):
    if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2) and min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1,y2):
        return True
    else:
        return False
def cross(x1,y1,x2,y2,x3,y3,x4,y4):
    abc=ccw(x1,y1,x2,y2,x3,y3)
    abd=ccw(x1,y1,x2,y2,x4,y4)
    cda=ccw(x3,y3,x4,y4,x1,y1)
    cdb=ccw(x3,y3,x4,y4,x2,y2)
    if abc*abd==0 and cda*cdb==0:
        return isEnvelope(x1,y1,x2,y2,x3,y3,x4,y4)
    elif abc*abd<=0 and cda*cdb<=0:
        return True
    return False
if cross(x1,y1,x2,y2,x3,y3,x4,y4):
    print(1)
else:
    print(0)

