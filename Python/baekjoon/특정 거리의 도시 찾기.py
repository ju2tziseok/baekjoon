from collections import deque
import sys
input = sys.stdin.readline
def bfs(graph,start,distance) :
    q = deque([start])
    distance[start] = 0
    while q:
        v= q.popleft()

        for i in graph[v] :
            if distance[i] == -1 :
                distance[i] = distance[v] + 1
                q.append(i)


n,m,k,x = map(int,input().split())
# n 도시 개수
# m 도로 개수
# k 거리 정보
# x 도시 번호
res=[]
graph=[[] for _ in range(n+1)]

for i in range(m) :
    a,b = map(int,input().split())
    graph[a].append(b)

for g in graph :
    g.sort()
cnt = 0
distance=[-1] * (n+1)

bfs(graph,x,distance)

if k not in distance :
    print(-1)
else:
    for i in range(1,n+1) :
        if distance[i] == k :
            print(i)


