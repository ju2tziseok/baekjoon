n=int(input())
dp=[i for i in range(0,n+1)]



for i in range(1,n+1) :
    for j in range(1,i+1) :
        square = j*j
        if square > i :
            break
        if dp[i] > dp[i-square] +1 :
            dp[i] = dp[i-square] +1

print(dp[n])