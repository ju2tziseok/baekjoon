n=int(input())

dp=[0]*(n+1)

date=[]
price=[]

for i in range(n):
    a,b=map(int,input().split())
    date.append(a)
    price.append(b)

for i in range(n) :
    for j in range(i+date[i],n+1) :
        if dp[j] < dp[i] + price[i] :
            dp[j] = dp[i] + price[i]
print(dp[-1])