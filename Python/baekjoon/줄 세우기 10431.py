def bubblesort(li):
    cnt = 0
    n = len(li)
    for i in range(n):
        for j in range(1, n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                cnt += 1

    return cnt


n = int(input())
s = []
for i in range(n):
    li = list(map(int, input().split()))
    s.append(bubblesort(li))

for i in range(n):
    print(i + 1, s[i])