

data=list(map(int,input().split()))
count=1
while data[0]!=0 :
    a=data[0]-1
    data.remove(data[0])
    data.append(a)
    count+=1

print(data)





