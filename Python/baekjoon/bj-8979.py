n,m=map(int,input().split())
li=[]
for i in range(n):
    [a,b,c,d]=map(int,input().split())
    li.append([a,b,c,d])

li.sort(key=lambda x:(-x[1],-x[2],-x[3]))

idx=0
for i in range(n):
    if li[i][0] == m :
        idx=i
        break

for i in range(n) :
    if li[idx][1:]== li[i][1:] :
        print(i+1)
        break