n=int(input())

check=list(map(int,input().split()))

m=int(input())

num=list(map(int,input().split()))
dic={}

for i in range(n):
    dic[check[i]]=0
for i in range(m):
    if num[i] in dic :
        print(1)
    else :
        print(0)