

t=int(input())
for i in range(t):
    data=list(map(int,input().split()))
    data.sort()
    print(f"#{i+1} {round(sum(data[1:9])/8)}")