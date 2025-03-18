from collections import deque
import sys

input = sys.stdin.readline  # BOJ에서 빠른 입력을 위해 사용

# 방향 벡터 (오른쪽, 아래, 왼쪽, 위)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def snake(n, array, data, direction):
    snake_body = deque([(0, 0)])  # 뱀의 위치 저장 (머리가 앞쪽)
    array[0][0] = -1  # 뱀이 있는 위치 표시
    time = 0
    move_idx = 0  # 방향 전환 인덱스

    while True:
        time += 1
        head_row, head_col = snake_body[0]  # 현재 머리 위치

        # 새로운 머리 위치
        new_row = head_row + dx[direction]
        new_col = head_col + dy[direction]

        # 벽 또는 자기 자신과 충돌하면 게임 종료
        if not (0 <= new_row < n and 0 <= new_col < n) or array[new_row][new_col] == -1:
            return time

        # 사과가 있는 경우
        if array[new_row][new_col] == 1:
            array[new_row][new_col] = -1  # 사과를 먹었으므로 비움
            snake_body.appendleft((new_row, new_col))  # 머리 추가 (길이 증가)
        else:
            # 사과가 없는 경우: 머리 추가 후 꼬리 제거
            snake_body.appendleft((new_row, new_col))
            tail_row, tail_col = snake_body.pop()
            array[tail_row][tail_col] = 0  # 꼬리 이동 후 자리 비움
            array[new_row][new_col] = -1  # 머리 위치 표시

        # 방향 전환 확인 (꼬리를 제거한 후에 적용해야 함)
        if move_idx < len(data) and data[move_idx][0] == time:
            if data[move_idx][1] == "L":
                direction = (direction - 1) % 4  # 왼쪽 90도 회전
            else:
                direction = (direction + 1) % 4  # 오른쪽 90도 회전
            move_idx += 1  # 방향 전환 인덱스 증가

# 입력 처리
n = int(input())  # 보드 크기
array = [[0] * n for _ in range(n)]  # 보드 초기화
k = int(input())  # 사과 개수

for _ in range(k):
    row, col = map(int, input().split())
    array[row - 1][col - 1] = 1  # 사과 위치 표시 (1-based index를 0-based로 변환)

data = []  # 방향 전환 정보
l = int(input())  # 방향 전환 횟수
direction = 0  # 처음에는 오른쪽 (dx, dy의 인덱스)

for _ in range(l):
    x, c = input().split()
    data.append((int(x), c))

# 결과 출력
print(snake(n, array, data, direction))
