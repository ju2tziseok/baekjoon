# 맵 크기 입력 받기
n,m=map(int,input().split())

#방문한 위치 저장할 맵 생성
d=[[0]*m for _ in range(n)]

#x,y 좌표 및 방향 받기

x,y,direction=map(int,input().split())

#현재 좌표 방문하기
d[x][y]=1

#바다 육지 맵 만들기
array=[]

for i in range(n):
    array.append(list(map(int,input().split())))


#북 동 남 서 정의 0,1,2,3

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#왼쪽 회전하기

def turn_left():
    global direction
    direction-=1
    if direction == -1 :
        direction=3

#시뮬레이션

count=1
turn_time=0

while True :
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    # 가보지 않았고 육지일 경우 전진
    if d[nx][ny]==0 and array[nx][ny]==0 :
        d[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    else :
        turn_time+=1

    #4방향 가본경우
    if turn_time == 4 :
        nx=x-dx[direction]
        ny=y-dy[direction]

        if array[nx][ny]==0 :
            x=nx
            y=ny
        else :
            break

        turn_time=0

print(count)