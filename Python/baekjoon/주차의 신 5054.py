t=int(input())

for i in range(t):
    n=int(input())#상점수

    li=list(map(int,input().split()))
    li.sort()
    sum=0
    for j in range(1,n):
        sum+=(li[j]-li[j-1])
    print(sum*2)