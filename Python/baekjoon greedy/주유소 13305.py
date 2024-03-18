n=int(input())
dis=list(map(int,input().split()))
price=list(map(int,input().split()))

res=0
m=price[0]
for i in range(n-1):
    if price[i]<m:
        m=price[i]
    res+=m*dis[i]


print(res)