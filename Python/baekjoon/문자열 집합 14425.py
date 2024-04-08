n,m=map(int,input().split())
s=set()
for i in range(n):
    s.add(input())
cnt=0
for i in range(m):
    check=input()
    if check in s:
        cnt+=1

print(cnt)


