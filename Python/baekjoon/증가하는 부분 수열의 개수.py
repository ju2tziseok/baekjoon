n= int(input())
data=list(map(int,input().split()))

dp=[1]*n

for i in range(1,n) :
    for j in range(i) :
        if data[j] < data[i] :
            dp[i] += dp[j]

for i in dp :
    print(i%998244353, end=' ')



