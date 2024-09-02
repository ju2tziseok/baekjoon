for i in range(1,11):
    n=int(input())
    data=list(map(int,input().split()))

    for j in range(n) :
        data.sort()
        data[0]+=1
        data[-1]-=1
    print(f"#{i} {max(data)-min(data)}")

