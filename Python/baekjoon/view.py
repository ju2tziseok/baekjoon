
def view(n,data) :
    cnt=0

    for i in range(2,n-2) :
        if data[i] > max(data[i-2],data[i-1],data[i+1],data[i+2]) :
            cnt+=data[i]-max(data[i-2],data[i-1],data[i+1],data[i+2])

    return cnt

for i in range(1,11) :
    n=(input())
    data=list(map(int,input().split()))
    print(f"#{i} {view(int(n),data)}")


