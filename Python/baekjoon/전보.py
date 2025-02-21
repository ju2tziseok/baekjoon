import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

# n : 도시의 개수(노드), m : 통로의 개수(간선), c : 메시지를 보내고자 하는 도시 (출발점)
n,m,start = map(int,input().split())

graph=[[] for _ in range(n+1)]
distance = [INF] * (n+1)

# x,y 특정 도시 z 메시지가 전달되는 시간
for _ in range(m) :
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start) :
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    while q :#큐가 비어있지 않다면
         #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist :
            continue
          # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
max_distance = 0

# 도달할 수 있는 노드중에서, 가장 멀리 있는 노드와의 최단 거리
for i in distance :
    if i != INF :
        count+=1
        max_distance = max(max_distance,i)
# 시작 노드는 제외해야 하므로 count -1을 출력
print(count-1, max_distance)
