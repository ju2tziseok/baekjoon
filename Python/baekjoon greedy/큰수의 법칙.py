n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()

firstmax=max(data) # 정답 해설 : 굳이 max연산 쓸필요 없음 왜냐하면 sort로 정렬했으니까
secondmax=max(data[:n-1])


#firstmax=data[n-1]
#secondmax=data[n-2] 이게 더 깔끔


res=0 # 결과값
cnt=0 # 횟수

for i in range(m) :
    if cnt<k :
        res+=firstmax
        cnt+=1
    else :
        res+=secondmax
        cnt=0

print(res)