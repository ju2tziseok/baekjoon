li=[]
cnt=[]
res=[]
for i in range(8):
    li.append(int(input()))
    cnt.append(li[i])

li.sort()


print(sum(li[3:]))

for i in range(3,8):
    res.append(cnt.index(li[i]) + 1)

res.sort()

for i in res :
    print(i,end=' ')

