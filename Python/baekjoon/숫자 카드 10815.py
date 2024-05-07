n=int(input())
card1=list(map(int,input().split()))
m=int(input())
card2=list(map(int,input().split()))
dic={}
for i in range(n) :
    dic[card1[i]]=0

for i in range(m) :
    if card2[i] not in dic :
        print(0,end=' ')
    else :
        print(1, end=' ')