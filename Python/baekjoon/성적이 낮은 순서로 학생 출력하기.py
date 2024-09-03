n=int(input())
data=[]
for i in range(n):
    a,b=input().split()
    data.append((a,int(b)))

data.sort(key=lambda x:x[1])

for i in data :
    print(i[0],end=' ')