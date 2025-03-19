import copy
from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
graph=[]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs() :
    q = deque()
    #원래 그래프 유지
    temp_grp = copy.deepcopy(graph)

    #바이러스 전파 시작
    for i in range(n) :
        for j in range(m) :
            if temp_grp[i][j] == 2 :
                q.append((i,j))

    while q :
        x,y = q.popleft()

        #바이러스 감염시키기
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny <0 or ny >=m :
                continue
            if temp_grp[nx][ny] == 0 :
                temp_grp[nx][ny] = 2
                q.append((nx,ny))

    global answer
    cnt = 0

    for i in range(n) :
        cnt+=temp_grp[i].count(0)
    answer= max(answer,cnt)

def makeWall(cnt) :
    # 벽 세개 만들어지면 바이러스 전파 시켜보기
    if cnt == 3 :
        bfs()
        return

    for i in range(n) :
        for j in range(m) : # 벽 만들수 잇는지 확인
            if graph[i][j] == 0 :
                graph[i][j] = 1 # 벽 만들기
                makeWall(cnt+1) # 다음 벽 만들기
                graph[i][j] = 0 #백 트랙킹 ,그래프 복구


for i in range(n) :
    graph.append(list(map(int,input().split())))

answer = 0

makeWall(0)

print(answer)