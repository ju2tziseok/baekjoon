import sys

n=int(sys.stdin.readline())

for _ in range(n):
    m=int(input())
    score=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]
    score.sort()

    cnt=1
    max_=score[0][1]
    for i in range(1,m):
        if max_ > score[i][1]:
            cnt+=1
            max_=score[i][1]
    print(cnt)


