n=int(input())

for i in range(n):
    a,b,c=map(int,input().split())
    cnt = 0

    while True:
        if a>c or b>c:
            break

        if a>=b :
            b+=a
            cnt+=1
        else :
            a+=b
            cnt+=1
    print(cnt)
