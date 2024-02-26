t=int(input())
for i in range(t):
    n=int(input())
    res=0
    avg=0
    for j in range(n):
        a,b=map(float,input().split())
        a=int(a)
        res+=a
        avg+=a*b
    print(res,round(avg/res,1))

