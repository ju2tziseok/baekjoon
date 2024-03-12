n,m=map(int,input().split())
cnt=[]
for i in range(m):
    a,b=map(int,input().split())
    if a>=n :
        cnt.append(0)
    else :
        cnt.append(n-a)

cnt.sort()
print(sum(cnt[:m-1]))