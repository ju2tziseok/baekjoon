n, k = map(int, input().split())

dp = [1] * (n + 1)  # 0! = 1, 1! = 1로 시작

for i in range(2, n + 1):
    dp[i] = dp[i - 1] * i

print((dp[n] // (dp[k] * dp[n - k])) % 10007)
