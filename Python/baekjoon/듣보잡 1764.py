n,m=map(int,input().split())
listen=set()
see=set()

for i in range(n):
    data=input()
    listen.add(data)

for i in range(m) :
    data=input()
    see.add(data)

see=listen&see
li=list(see)
li.sort()
print(len(li))
for i in li :
    print(i)