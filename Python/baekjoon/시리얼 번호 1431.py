n=int(input())
li=[]
for i in range(n):
    a=input()
    li.append(a)

def sum_num(x):
    res=0

    for i in x :
        if i.isdigit() :
         res+=int(i)
    return res

li.sort(key=lambda x:(len(x),sum_num(x),x))

for i in li:
    print(i)