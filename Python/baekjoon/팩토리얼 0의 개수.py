import math
n=int(input())

li=math.factorial(n)
li=str(li)
li=list(li)
cnt=0
for i in li[::-1] :
    if i!='0' :
        break
    elif i=='0' :
        cnt+=1

print(cnt)


