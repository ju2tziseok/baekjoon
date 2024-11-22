n,m=map(int,input().split())

price=[list(map(int,input().split()))for _ in range(m)]


six_price=1001
one_price=1001
for i in range(m) :
    if price[i][1] < one_price :
        one_price=price[i][1]
    if price[i][0] <six_price :
        six_price=price[i][0]

pay=0

six=min((n//6)*six_price,((n//6)*6)*one_price)
rest=min(six_price,(n%6)*one_price)

print(six+rest)
