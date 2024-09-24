def charge(n) :
    cnt = [0] * len(money)
    i=0
    while n>0 and i <len(money):

        if n >= money[i] :
            n-=money[i]
            cnt[i]+=1
        else:    i+=1
    return cnt


t=int(input())
money=[50000,10000,5000,1000,500,100,50,10]

for i in range(1,t+1):
    n=int(input())
    print(f"#{i}")
    for j in charge(n) :
        print(j,end=' ')
    print()