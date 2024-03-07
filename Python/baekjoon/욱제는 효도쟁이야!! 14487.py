n=int(input())
li=list(map(int,input().split()))

li.sort()
s=0
for i in range(n-1):
    s+=li[i]

print(s)