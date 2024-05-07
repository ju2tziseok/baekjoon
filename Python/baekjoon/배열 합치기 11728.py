n,m=map(int,input().split())

li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
c=li1+li2
c.sort()
for i in c:
    print(i,end=' ')

