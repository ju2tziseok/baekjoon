import sys
input = sys.stdin.readline
n,k=map(int,input().split())

data=list(map(int,input().split()))

left = 0
right = 0
count_odd = 0
max_len = 0
while right < n :
    if data[right] % 2 ==1 :
        count_odd+=1

    while count_odd > k :
        if data[left] % 2 == 1 :
            count_odd -=1
        left +=1

    max_len=max(max_len, right -left+1 - count_odd)
    right +=1

print(max_len)