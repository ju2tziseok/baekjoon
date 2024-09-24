t=int(input())

for i in range(1,t+1) :
    a,b,c,d=map(int,input().split())
    time=(a+c) +((b+d)//60)
    minute=(b+d)%60

    if time>12 :
        time-=12

    print(f"#{i} {time} {minute}")
