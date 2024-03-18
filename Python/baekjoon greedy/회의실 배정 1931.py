import sys
n=int(sys.stdin.readline())
li=[]


for i in range(n):
    [a,b]=map(int,sys.stdin.readline().split())
    li.append([a,b])

li.sort(key=lambda x:(x[1],x[0]))

cnt=1
end=li[0][1]
for i in range(1,n) :
    if li[i][0]>=end :
        cnt+=1
        end=li[i][1]

print(cnt)

