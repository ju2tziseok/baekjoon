import sys
n=int(sys.stdin.readline().rstrip())
stack=[]
def push(s):
    stack.append(s)

def pop() :
    if len(stack)>0 :
        print(stack.pop())
    else :
        print(-1)
def size() :
    print(len(stack))

def empty() :
    if len(stack)>0 :
        print(0)
    else :
        print(1)

def top():
    if len(stack)>0 :
        print(stack[-1])
    else :
        print(-1)


for i in range(n):
    a=sys.stdin.readline().split()
    if a[0]=='push':
        push(a[1])
    elif a[0]=="pop":
        pop()
    elif a[0]=="size":
        size()
    elif a[0]== "empty":
        empty()
    elif a[0]== "top":
        top()