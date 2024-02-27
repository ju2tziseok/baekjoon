li=[]
li=list(map(int,input().split()))
res=0

for i in range(5) :
    res+=pow(li[i]**2)
print(res%10)