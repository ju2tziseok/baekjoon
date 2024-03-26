import sys
stack=[]
n=int(sys.stdin.readline().rstrip())

for i in range(n):
    t=list(map(int,sys.stdin.readline().split()))
    if t[0]==1 :
        stack.append(t[1])
    if t[0]==2 :
        if len(stack)>0 :
           print(stack.pop())
        elif len(stack)==0 :
            print(-1)

    if t[0]==3 :
        print(len(stack))

    if t[0]==4 :
        if len(stack)==0 :
            print(1)
        else :
            print(0)
    if t[0]==5 :
        if len(stack)>0 :
            print(stack[-1])
        else :
            print(-1)