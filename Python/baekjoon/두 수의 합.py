n=int(input())
data=list(map(int,input().split()))
x=int(input())

cnt=0

data.sort()
start=0
end=len(data)-1
while start < end :
    if data[start] + data[end] == x :
        cnt+=1
        start+=1
        end-=1
    elif data[start] + data[end] < x :
        start+=1
    else :
        end-=1
print(cnt)