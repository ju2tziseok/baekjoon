def P(n,dp) :
    if n == 1 or n == 2 or n == 3:
        return 1

    for i in range(4,n+1) :
        dp[i] = dp[i-2] +dp[i-3]
    return dp[n]
    '''
    if n ==1 or n==2 or n == 3 :
        return 1
    if dp[n] != 0 :
        return dp[n]
    dp[n] = P(n-2) + P(n-3)
    return dp[n]
    '''


t=int(input())
dp=[0]*101
dp[1]=1
dp[2]=1
dp[3] =1
for i in range(t):
    n=int(input())
    print(P(n,dp))