t=int(input())
for i in range(t):
    li=list(map(int,input().split()))
    cnt=[]
    for j in li :
        if j%2==0:
            cnt.append(j)
    print(sum(cnt),min(cnt))