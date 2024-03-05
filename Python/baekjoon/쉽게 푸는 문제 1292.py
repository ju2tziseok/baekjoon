a,b=map(int,input().split())
cnt=[]
for i in range(1,b+1) :
    for j in range(i):
        cnt.append(i)

res=sum(cnt[a-1:b])
print(res)