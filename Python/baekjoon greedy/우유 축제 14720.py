n=int(input())
li=list(map(int,input().split()))
cnt=0
for i in range(n) :
    if li[i]==cnt%3:
        cnt+=1

print(cnt)
