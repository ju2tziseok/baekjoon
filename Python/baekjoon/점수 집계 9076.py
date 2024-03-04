t=int(input())
for i in range(t):
    li=list(map(int,input().split()))
    li.sort()
    if (li[3]-li[1]>=4) :
        print("KIN")
    else:
        print(sum(li[1:4]))
