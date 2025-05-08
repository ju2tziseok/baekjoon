n=int(input())
data=list(map(int,input().split()))

dp=[i for i in data]

for i in range(1,n) :
        dp[i] = max(dp[i],dp[i]+dp[i-1])
print(max(dp))