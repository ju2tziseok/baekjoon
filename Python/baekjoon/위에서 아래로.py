t=int(input())

array=[]

for i in range(t):
    array.append(int(input()))


result=sorted(array,reverse=True)

for i in result :
    print(i,end=' ')


li=[]
li.append