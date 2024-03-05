n=int(input())

for i in range(n):
    c=int(input())

    t=int(input())
    res=c
    for j in range(t):
        a,b=map(int,input().split())
        res+=a*b
    print(res)