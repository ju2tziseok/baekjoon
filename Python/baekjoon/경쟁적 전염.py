from collections import deque

n,k = map(int,input().split())
# n x n 보드 크기
# k 바이러스 개수

graph=[]
data=[]
for i in range(n) :
    graph.append(list(map(int,input().split())))
    for j in range(n) :
        if graph[i][j] != 0 :
            data.append((graph[i][j],0,i,j))
s,target_x,target_y = map(int,input().split())




#바이러스가 번호가 낮은 종류부터 증식
data.sort()

#상하좌우로 증식
dx=[-1,1,0,0]
dy=[0,0,-1,1]

q=deque(data)

while q:
    virus, cnt ,x,y = q.popleft()

    if cnt == s :
        break
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if 0<=nx <n and 0<= ny < n :
            if graph[nx][ny] == 0 :
                graph[nx][ny] = virus
                q.append((virus,cnt+1,nx,ny))

print(graph[target_x-1][target_y-1])
