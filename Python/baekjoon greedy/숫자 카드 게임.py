n,m=map(int,input().split())
min_li=[]

res=0
for i in range(n):
    data=list(map(int,input().split()))
    minvalue=min(data)
    res=max(res,minvalue)

print(res)