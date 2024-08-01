n,m=map(int,input().split())
data=list(map(int,input().split()))

balling=[0]*11


for x in data :
    balling[x]+=1

result = 0

for i in range(1,m+1) :
    n-=balling[i]
    result+=balling[i]*n

print(result)
