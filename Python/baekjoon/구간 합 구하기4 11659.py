import sys
input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
sum_li=[0]
cumul=0

for i in range(n) :
    cumul+=num[i]
    sum_li.append(cumul)

for i in range(m) :
    a,b=map(int,input().split())
    print(sum_li[b]-sum_li[a-1])

