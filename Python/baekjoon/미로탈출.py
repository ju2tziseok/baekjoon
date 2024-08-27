from collections import deque


n,m=map(int,input().split())

data=[]

for i in range(n) :
    data.append(list(map(int,input())))



#상하 좌우 만들기
#상 -1 0, 하 1 0 좌 0 -1 우 0 1
dx=[-1,1,0,0]
dy=[0,0,-1,1]


#bfs
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))

    while queue :

        x,y=queue.popleft()

        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m :
                continue
            if data[nx][ny] ==0 :
                continue
            if data[nx][ny] == 1 :
                data[nx][ny]=data[x][y]+1
                queue.append((nx,ny))

    return data[n-1][m-1]

print(bfs(0,0))

