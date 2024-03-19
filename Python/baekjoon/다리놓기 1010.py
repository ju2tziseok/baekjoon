import math
t=int(input())

for i in range(t) :
    k,n=map(int,input().split())
    res=math.factorial(n)//(math.factorial(k)*(math.factorial(abs(n-k))))
    print(res)