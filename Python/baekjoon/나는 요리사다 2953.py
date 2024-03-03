li=[]
cnt=[]
for i in range(5):
     li=map(int,input().split())
     cnt.append(sum(li))

print(cnt.index(max(cnt))+1,max(cnt))