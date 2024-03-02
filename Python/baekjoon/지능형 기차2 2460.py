li=[]
res=0
for i in range(10):
    a,b=map(int,input().split())

    res=res-a+b
    li.append(res)

print(max(li))