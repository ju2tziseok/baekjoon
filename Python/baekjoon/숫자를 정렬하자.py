def sorting(data) :
    data.sort()
    return data


t=int(input())

for i in range(1,t+1) :
    n=int(input())
    data=list(map(int,input().split()))
    print(f"#{i} {' '.join(map(str,sorting(data)))}")
