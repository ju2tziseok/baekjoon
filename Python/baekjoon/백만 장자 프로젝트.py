
def money(n) :
    data=list(map(int,input().split()))
    max_money=data[-1]
    cnt=0
    for i in range(n-2,-1,-1) :
        if max_money >= data[i] :
            cnt+=(max_money-data[i])
        else :
            max_money=data[i]
    return cnt


t=int(input())

for i in range(1,t+1) :
    n=int(input())
    print(f"#{i} {money(n)}")

