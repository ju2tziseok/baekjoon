n = int(input())
vote = [int(input()) for _ in range(n)]

cnt = 0

if n == 1:
    print(0)
else:
    max_vote = max(vote[1:])  # 다솜이를 제외한 후보들 중 가장 높은 득표수

    while max_vote >= vote[0]:  # 다솜이의 득표수가 최고 득표수보다 작거나 같을 때 반복
        max_idx = vote[1:].index(max_vote) + 1  # 다솜이를 제외한 리스트에서 최대값의 인덱스 찾기
        vote[max_idx] -= 1  # 해당 후보의 표를 하나 감소
        vote[0] += 1  # 다솜이의 표를 하나 증가
        cnt += 1  # 매수 횟수 증가
        max_vote = max(vote[1:])  # 최대값 갱신

    print(cnt)
