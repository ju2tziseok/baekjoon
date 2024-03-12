n=int(input())
li=list(map(int,input().split()))

res=[]
cnt=0
height=li[0]
for i in range(1,n):
    if li[i]<height :
        cnt+=1
    else :
        height=li[i]
        res.append(cnt)
        cnt=0
res.append(cnt)
print(max(res))