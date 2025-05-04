n=int(input())

data=list(map(int,input().split()))
dp=[1] * n
dp_r=[1]*n

for i in range(1,n) :
    for j in range(i) :
        if data[j] < data[i] :
            dp[i] = max(dp[j]+1 , dp[i])


for i in range(n-1,-1,-1) :
    for j in range(n-1,i,-1) :
        if data[j] < data[i] :
            dp_r[i] = max(dp_r[j]+1,dp_r[i])

#dp를 두개 구함 왼쪽으로 오른쪽으로 그래서 겹치는게 하나 있으니 더하고 1을빼줌
res=0
for i in range(n) :
    res = max(res,dp[i]+dp_r[i])
print(res-1)