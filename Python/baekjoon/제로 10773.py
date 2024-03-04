
t=int(input())
li=[]
for i in range(t):
    a=int(input())
    if a==0 :
        li.pop(len(li)-1)
    else:
        li.append(a)

print(sum(li))
