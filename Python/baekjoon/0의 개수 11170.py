t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    cnt=0
    for j in range(a,b+1):
        cnt+=str(j).count('0')


    print(cnt)