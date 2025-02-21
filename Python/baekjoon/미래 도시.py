import sys
input = sys.stdin.readline

#문제 조건
# 1. 양방향으로 이동 가능
# 2. 가는 비용 모두 1
# 3. 1번 회사에 출발하여 K번회사 방문한 뒤 X번 회사로 가는 것
INF = int(1e9)

#회사의 개수 n, 경로의 개수 m
n,m = map(int,input().split())

graph=[[INF] * (n+1) for _ in range(n+1)]
#자기 자신한테 가는 경로의 비용은 0으로 초기화
for a in range(1,n+1) :
    for b in range(1,n+1) :
        if a == b :
            graph[a][b] =0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m) :
    a,b= map(int,input().split())
    # 가는 비용은 전부 1
    graph[a][b] = 1
    graph[b][a] = 1


# 최종 목적지 x, 거쳐야 하는 회사 k
x,k=map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1) :
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[b][k])
# 수행된 결과를 출력
distance=graph[1][k] + graph[k][x]

#도달 할수 없는 경우 -1 출력
if distance >= INF :
    print(-1)
else :
    print(distance)
