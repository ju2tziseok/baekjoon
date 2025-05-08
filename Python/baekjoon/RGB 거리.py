#집은 1번부터 n번 집까지
#집 색깔은 빨 파 초 각각 칠하는 비용이 있음

#칠하는 규칙
#1번 색 != 2번 색
#n번 색 != n-1번 색
#i번 색 != i-1번 색 and i번 색 != i+1번 색 (2<= i <=n-1)

n=int(input())
data=[]
for i in range(n) :
    data.append(list(map(int,input().split())))
#data[0] : 1번 집에 대한 빨 파 초 칠하는 비용이 담겨 있음

dp=[[1001] * 3 for _ in range(n)]

for i in range(3) :
    dp[0][i] = data[0][i]


i=1
while i < n :
    for j in range(3):
        if j == 0 :
            dp[i][j] = min(dp[i-1][1] +data[i][j],dp[i-1][2] +data[i][j])
        elif j == 1 :
            dp[i][j] = min(dp[i-1][0]+data[i][j],dp[i-1][2]+data[i][j])
        elif j == 2 :
            dp[i][j] = min(dp[i-1][0]+data[i][j],dp[i-1][1]+data[i][j])
    i+=1

print(min(dp[n-1]))