n=int(input())

data=list(map(int,input().split()))

dp=[i for i in data]

for i in range(1,n) :
    for j in range(i) :
        if data[j] > data[i] :
            dp[i]=max(dp[i],dp[j]+data[i])
print(max(dp))