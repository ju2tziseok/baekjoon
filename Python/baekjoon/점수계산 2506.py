n=int(input())
sumb=0
res=0
k=list(map(int,input().split()))
for i in range(n):
    if k[i]==1 :
        sumb+=1
        res+=sumb
    else :
        sumb=0
print(res)

