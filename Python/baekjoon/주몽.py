n=int(input())
m=int(input())
data=list(map(int,input().split()))
start=0
end=n-1
data.sort()
cnt=0

while start<end :
    if data[start] + data[end] == m :
        cnt+=1
        start+=1
        end-=1
    elif data[start] + data[end] < m :
        start+=1
    else :
        end -= 1

print(cnt)