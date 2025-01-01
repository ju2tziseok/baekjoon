



t=int(input())

for i in range(1,t+1):
    n=int(input())
    stone=list(map(int,input().split()))
    for j in range(n) :
        stone[j]=abs(stone[j])
    print(f"#{i} {min(stone)} {stone.count(min(stone))}")