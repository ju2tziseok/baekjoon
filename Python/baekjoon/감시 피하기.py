import copy
import sys
input = sys.stdin.readline

n=int(input())
graph=[]
teacher=[]

for i in range(n) :
    graph.append(list(input().split()))


found = False
#선생님은 상하좌우로 감시 가능 근데 한칸이 아니라 장애물이 없는한끝까지
# 그럼 x면 계속 탐색을 진행하기 위해 큐에 삽입
# s가 한번이라도 보이면 found를 false로
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# t : 선생님 존재하는 칸
# s : 학생이 존재하는 칸
# o : 장애물이 존재하는 칸


def bfs() :
    global found
    temp_graph=copy.deepcopy(graph)

    #선생 감시
    for i in range(n) :
        for j in range(n) :
            if temp_graph[i][j] == "T" :
                for d in range(4) :
                    nx,ny=i,j
                    while True :
                        nx+=dx[d]
                        ny+=dy[d]

                        if nx <0 or nx>=n or ny<0 or ny>=n :
                            break
                        if temp_graph[nx][ny] == "O" :
                            break
                        if temp_graph[nx][ny] == "S" :
                            return
    found = True

#장애물 3개 설치
def makeWall(cnt) :

    if cnt == 3 :
        bfs()
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == "X" :
                graph[i][j] = "O"
                makeWall(cnt+1)
                graph[i][j] = "X"

makeWall(0)

if found :
    print("YES")
else :
    print("NO")


