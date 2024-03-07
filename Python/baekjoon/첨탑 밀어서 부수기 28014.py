n=int(input())

li=list(map(int,input().split()))
res=1
for i in range(n-1):
    if li[i]<li[i+1] :
        res+=1

print(res)