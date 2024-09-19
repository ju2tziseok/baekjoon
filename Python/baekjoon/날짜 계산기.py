def counting(a,b,c,d) :
    cnt=date[a]-b
    for i in range(a+1,c) :
        cnt+=date[i]
    cnt+=d+1
    return cnt

date=[0,31,28,31,30,31,30,31,31,30,31,30,31]


t=int(input())

for i in range(1,t+1) :
    a,b,c,d=map(int,input().split())

    if a==c :
        print(f"#{i} {d-b+1}")
    else :
        print(f"#{i} {counting(a,b,c,d)}")
