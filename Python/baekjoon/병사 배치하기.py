n = int(input())
data = list(map(int, input().split()))

data.reverse()  # LIS로 바꾸기 위해 역순 처리
dp = [1] * n     # 자기 자신 포함해서 최소 길이 1

for i in range(n):
    for j in range(i):
        if data[j] < data[i] :
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))  # 총 병사 수 - 최대 LIS 길이 = 열외시켜야 하는 병사 수
