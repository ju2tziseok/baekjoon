import sys
from collections import deque
n=int(input())
li=[]
li=deque(li)
for i in range(n):
    a=sys.stdin.readline().split()

    if a[0]=="push":
        li.append(a[1])
    elif a[0]=="pop" :
        if len(li)>0 :
            print(li.popleft())
        else :
            print(-1)
    elif a[0]=="size":
        print(len(li))
    elif a[0]=="empty":
        if len(li)==0 :
            print(1)
        else :
            print(0)
    elif a[0]== "front":
        if len(li)>0:
            print(li[0])
        else :
            print(-1)
    elif a[0]=="back" :
        if len(li)>0 :
            print(li[-1])
        else :
            print(-1)
