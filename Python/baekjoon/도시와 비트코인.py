from collections import deque

n,m=map(int,input().split())

graph=[]

dx=[0,1]
dy=[1,0]

for i in range(m) :
    graph.append(list(map(int,input().split())))

visited=[[False]*n for _ in range(m)]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True

    while queue :
        x,y = queue.popleft()

        if x==m-1 and y==n-1 :
            return True

        for i in range(2) :
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<m and ny>=0 and ny<n :
                if graph[nx][ny]==1 and not visited[nx][ny] :
                    visited[nx][ny]=True
                    queue.append((nx,ny))
    return False

if bfs(0,0) :
    print("Yes")
else :
    print("No")