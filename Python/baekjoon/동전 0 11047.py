import sys
n,k=map(int,sys.stdin.readline().split())
li=[]
cnt=0

for i in range(n):
    li.append(int(sys.stdin.readline()))

while k>0 :

    if li[n-1]<=k :
        cnt+=1
        k-=li[n-1]
    else :
        n-=1

print(cnt)