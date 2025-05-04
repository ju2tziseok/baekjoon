n=int(input())

data=list(map(int,input().split()))

dp=[i for i in data] # dp[i]를 기준으로 했을때 부분 수열 합

for i in range(n) :
    for j in range(i) :
        if data[j] < data[i] :
            dp[i] = max(dp[i],dp[j]+data[i])

print(max(dp))