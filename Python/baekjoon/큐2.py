import sys
from collections import deque
n=int(sys.stdin.readline())

cnt=deque([])
for i in range(n):
    li=(sys.stdin.readline().split())
    if li[0]=="push":
        cnt.append(li[1])
    elif li[0]=="pop":
        if len(cnt)>0 :
            print(cnt.popleft())

        else :
            print(-1)
    elif li[0]=="size" :
        print(len(cnt))
    elif li[0]=="empty" :
        if len(cnt)==0 :
            print(1)
        else :
            print(0)

    elif li[0]=="front":
        if len(cnt)>0 :
            print(cnt[0])
        else :
            print(-1)
    elif li[0]=="back":
        if len(cnt)>0 :
            print(cnt[len(cnt)-1])
        else :
            print(-1)