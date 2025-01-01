a,b=map(int,input().split())
n=int(input())
button=[]
for i in range(n):
    button.append(int(input()))

cnt=[]
cnt.append(abs(b-a))

for i in range(n):
    cnt.append(abs(button[i]-b)+1)

print(min(cnt))